from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Portfolio
from .models import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.http import HttpResponseRedirect



def fullsite(request):
	context_general = {}

	## Posts ##

	context_general["posts"] = Post.objects.order_by('date')
	
	## Form ##

	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():

			name = request.POST.get('name', '')

			email_contact = request.POST.get('email_contact', '')

			phone = request.POST.get('phone', '')

			content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
			template = get_template('core/email_template.txt')

			context_email = Context({
				'name': name,
				'email_contact': email_contact,
				'phone': phone,
				'content': content,
			})
			content = template.render(context_email)

			# console send ##

			email = EmailMessage(
				"Novo contato",
				content,
				"3Ecologias" +'',to=
				['admin@3ecologias.net'],
				headers = {'Reply-To': email_contact }
 			)
			email.send()
			return HttpResponseRedirect('/')

			

	context_general["form"] = form_class

	context_general["ports"] = Portfolio.objects.order_by('date')

	return render(request, 'core/index.html', context_general)