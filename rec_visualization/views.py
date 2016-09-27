from django.shortcuts import render, render_to_response
import json
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

def simulate_individual_rec_request(rec_url, key, param):
	param_json_str = json.dumps({'license':param})
	payload = {key:param_json_str}
	print payload
	r = requests.get(rec_url, params=payload)
	result_dict = r.json()
	result_list = []
	if 'rcData' in result_dict:
		rc_dict_list = result_dict['rcData']
		result_list = [x['vid'] for x in rc_dict_list]

	return result_list

def query_user_history(history_url, key, param):
	payload = {key:param}
	r = requests.get(history_url, params=payload)
	result_dict = r.json()
	result_list = []
	if 'history' in result_dict:
		for item in result_dict['history']:
			result_list.append(int(item))

	return result_list


def quit_visualize(request):
	error = False
	if 'vid' in request.GET:
		vid = request.GET['vid']
		if not vid:
			error = True
		else:
			results = simulate_rec_request('http://10.100.5.104/quit','key',vid)
			video_infos = Sndlvl.objects.filter(id__in=results)
			video_infos = dict([(video.id, video) for video in video_infos])
			sorted_video_infos = [video_infos[idx] for idx in results]
			query_vid = Sndlvl.objects.filter(id=vid)
			return render_to_response('quit_visualize.html', {'rec_results':sorted_video_infos, 'query':query_vid[0]})
	return render_to_response('quit_query.html', {'error': error})


def content_visualize(request):
	error = False
	if 'vid' in request.GET:
		vid = request.GET['vid']
		if not vid:
			error = True
		else:
			results = simulate_rec_request('http://10.100.5.104/content','key',vid)
			video_infos = Sndlvl.objects.filter(id__in=results)
			video_infos = dict([(video.id, video) for video in video_infos])
			sorted_video_infos = [video_infos[idx] for idx in results]
			query_vid = Sndlvl.objects.filter(id=vid)
			return render_to_response('quit_visualize.html', {'rec_results':sorted_video_infos, 'query':query_vid[0]})
	return render_to_response('quit_query.html', {'error': error})


def user_visualize(request):
	error = False
	if 'vid' in request.GET:
		vid = request.GET['vid']
		if not vid:
			error = True
		else:
			results = simulate_individual_rec_request('http://10.100.5.104/homePage/personal','params',vid)
			video_infos = Sndlvl.objects.filter(id__in=results)
			video_infos = dict([(video.id, video) for video in video_infos])
			sorted_video_infos = [video_infos[idx] for idx in results]
			history_results = query_user_history('http://10.100.5.104/user_history', 'key', vid)
			history_videos = Sndlvl.objects.filter(id__in=history_results)
			history_videos = dict([(video.id, video) for video in history_videos])
			sorted_history_videos = [history_videos[idx] for idx in history_results]
			return render_to_response('homePage_visualize.html', {'rec_results':sorted_video_infos, 'lics':vid, 'history':sorted_history_videos})
	return render_to_response('quit_query.html', {'error': error})

def boot(request):
	return render_to_response('bootstrap_test.html')