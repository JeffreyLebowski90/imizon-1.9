from django.shortcuts import render, redirect
from .forms import TestForm
from .models import Post

# Create your views here.

rows = (
	("y", "n", "y", "y", "y", "n", "y", "y", "y", "n", "y", "y", "y", "y",),
	("n", "y", "y", "y", "n", "y", "y", "y", "n", "y", "y", "y", "y", "y",),
	("y", "y", "n", "n", "y", "y", "n", "n", "y", "y", "n", "n", "y", "y",),
	("y", "n", "n", "n", "y", "n", "n", "n", "y", "n", "n", "n", "n", "y",),
	("n", "n", "n", "y", "n", "n", "n", "y", "n", "n", "n", "y", "n", "n",),
)
rows_price = (
	("3 w", "10.000€",),
	("1 w", "14.000€",),
	("2 w", "12.000€",),
	("0.5 w", "5.000€",),
	("1 w", "2.000€",),
)
rows_perc = (85, 85, 80, 50, 30)
valves = [
	["N1",], ["N2",], ["N3",], ["N4",], ["N5",],
]



def home(request):
	Post.objects.all().delete()
	if request.method == 'POST':
		my_form = TestForm(request.POST)
		context = {
			"form": my_form,
		}
		if my_form.is_valid():
			my_form.save()
		return redirect('result')
	else:
		my_form = TestForm()
		context = {
			"form": my_form,
		}
		return render(request, 'home.html', context)



def result(request):
	red = []
	green = []
	colorz = []
	#####
	for row in rows_perc:
		if row <= 50:
			red.append(hex(15))
			green.append(hex(int(row*0.3)))
		else:
			green.append(hex(15))
			red.append(hex(int((100-row)*0.3)))
	for i in range(0, len(red)):
		red[i] = red[i].replace('0x', '')
		green[i] = green[i].replace('0x', '')
		colorz.append('#' + red[i] + green[i] + '0')
	for idx, valve in enumerate(valves):
		valve.append(str(rows_perc[idx]) + "%")
		valve.append(colorz[idx])
	my_form = TestForm()
	#####
	context = {
		'form': my_form,
		'rows': rows,
		'rows_price': rows_price,
		'valves': valves,
	}
	if request.GET.get('buybtn'):
		request.session['buy_choice'] = request.GET.get('buybtn')
		return redirect('valve')
	else:
		return render(request, 'result.html', context)



def valve(request):
	results = []
	paramz = []
	checks = []
	check_style = []
	my_form = TestForm()
	for ob in my_form:
		paramz.append(ob.label)
	posts = Post.objects.all()
	post = posts[0]
	for attr, value in post.__dict__.items(): 
		results.append(value)
	del results[0]
	del results[0]
	buy_choice = request.session.get('buy_choice')
	checks = rows[int(buy_choice)]
	buy_perc = str(rows_perc[int(buy_choice)]) + '%'
	for ob in checks:
		if ob == 'y':
			check_style.append('btn-success')
		else:
			check_style.append('btn-danger')
	zipped = list(zip(paramz, results, check_style))
	context = {
		'zipped': zipped,
		'buy_perc': buy_perc,
	}
	return render(request, 'valve.html', context)



def contact(request):
	buy_choice = request.session.get('buy_choice')
	buy_perc = str(rows_perc[int(buy_choice)]) + '%'
	context = {
		'buy_perc': buy_perc,
	}
	return render(request, 'contact.html', context)

def shipping(request):
	return render(request, 'shipping.html', {})

def deliver(request):
	return render(request, 'deliver.html', {})

def terms(request):
	return render(request, 'terms.html', {})

def feedbacks(request):
	return render(request, 'feedbacks.html', {})


