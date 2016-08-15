from django.shortcuts import render, render_to_response
import requests

from rec_visualization.models import Sndlvl


def simulate_rec_request(rec_url, key, param):
	payload = {key:param}
	r = requests.get(rec_url, params=payload)
	result_dict = r.json()
	result_list = []
	if 'rcData' in result_dict:
		rc_dict_list = result_dict['rcData']
		result_list = [x['vid'] for x in rc_dict_list]

	return result_list



def quit_visualize(request):
	error = False
	if 'vid' in request.GET:
		vid = request.GET['vid']
		if not vid:
			error = True
		else:
			results = simulate_rec_request('http://api.dev.hifuntv.com/quit','key',vid)
			video_infos = Sndlvl.objects.filter(id__in=results)
			query_vid = Sndlvl.objects.filter(id=vid)
			return render_to_response('quit_visualize.html', {'rec_results':video_infos, 'query':query_vid[0]})
	return render_to_response('quit_query.html', {'error': error})


def boot(request):
	return render_to_response('bootstrap_test.html')