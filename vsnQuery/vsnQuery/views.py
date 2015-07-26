from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from importVsns.models import VSNData
from django.template import RequestContext
from django.shortcuts import render_to_response
import re

def index(request):
     #serve up the form as response to request	
     #print "We are in index request"
     template = loader.get_template('vsnQuery/index.html')
     context=0
     return HttpResponse(template.render(context))
	
def search(request):
     #print "We are in search request"
     query = request.GET.get('query')

     # strip away blank spaces and convert to upper case
     query = str(query.strip().upper()) 
     
     # substring out first 6 and second set of 6 chars and chk for valid rules
     queryFp = query[0:6]
     queryLp = query[6:12]
     resultFp = re.search("[A-Z]{6}", queryFp)
     resultLp = re.search("[0-9]{6}", queryLp)     

     # Note: can avoid hard-coding the "12" below
     if ((not query) or (len(query) != 12) or (resultFp is None) or (resultLp is None)):

         # Empty string OR invalid length (extra chars after valid string)
         # OR first 6 chars not alphabets OR second set of 6 chars not numbers
         # then return empty string into response as invalid query

         query = None
         results = None
     
     else: 
         # non-empty AND valid query string
         
         # initialize minPos = tracker for minimum stars (*) db position
         minPos = VSNData.objects.count()+5
         
         # initialize minStarCnt = tracker for count of min num of stars 
         # in case of multiple matches; to return closest match per rules
         minStarCnt = 100    

         # initial found=match in db binary flag to -1 (not found)
         found = -1

         # loop over db entries, do a regexp search per entry against query
         # Note: VSNData.objects.filter(SerialNumberPattern__regex=queryMod)
         #       , where queryMod is a replaced [0-9*] or [A-Z*] query
         #       , does not work because the wildcards are in the db, not in
         #       query string. Hence we have to loop over db ourselves
         #       , at least I haven't a cool method to call regexp with 
         #       wildcards in 1 shot

         for i in range(0, VSNData.objects.count()):
            currDbEntry = VSNData.objects.all()[i] 
            currIndexedSNP = str(currDbEntry.Indexed_SNP)

            # check if match is found; if so update tracker variables
            if re.search(currIndexedSNP, query) is not None:
               # match found
               found = 0
               cntStars = currDbEntry.SerialNumberPattern.count('*')

               # update trackers only if new match is less wildcards than 
               # prior match (in case of multiple matches)
               if cntStars < minStarCnt:
                  minPos = i
                  minStarCnt = cntStars

         # end of for loop

         # if match is found then send match otherwise send a dummy result stating no match
         if found == 0:
            results = VSNData.objects.all()[minPos]
         else:
            results = VSNData(Indexed_SNP=None, SerialNumberPattern=None, VehicleTrimId=None, Year=None, Make=None, Model=None, TrimName=None)

     # else of if-else code
     context = RequestContext(request)
     return render_to_response('vsnQuery/results.html', {"results": results,}, context_instance=context)

