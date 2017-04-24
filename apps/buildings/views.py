from django.shortcuts import render, HttpResponse, redirect
from random import randrange

# the variable "gold" to keep count of player's winnings



def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'log' not in request.session:
		request.session['log'] = []
	return render(request, 'buildings/index.html')

 
def process(request, site):
	if site == 'farm':
		take = randrange(10,21)
	elif site == 'cave':
		take = randrange(5,11)
	elif site == 'house':
		take = randrange(2,6)
	elif site == 'casino':
		take = randrange(-50,51)
	else:
		return HttpResponse('invalid request')
	# Create a log of activities, where the player went and how much was won or lost at each attempt
	if take > 0:
		activity = "You went into a "+site+" and won "+str(take)+" golds!"
	else:
		activity = "Ouch. You went into a casino and lost "+str(abs(take))+" golds"
	request.session['log'] = [activity] + request.session['log']


	request.session['gold'] += take
	 
	return redirect('/')

def destroy(request):
	if 'gold' in request.session:
		del request.session['gold']
	if 'log' in request.session:
		del request.session['log']
	return redirect('/')