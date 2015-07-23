from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'surveys/index.html')

def frame(request):
	request.session['img_data'] = request.POST
	content = {'title':request.session['img_data']['title'], 'description': request.session['img_data']['description'], 'img_url': request.session['img_data']['img_url']}
	print request.session['img_data']['description']

	return render(request, 'surveys/frame.html', content)