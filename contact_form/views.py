"""
View which can render and send email from a contact form.
"""
from django.shortcuts import render_to_response, redirect
from django.views.generic import FormView
from django.template import RequestContext

from contact_form.forms import ContactForm


class ContactFormView(FormView):
    """
    Render a contact form, validate its input and send an email
    from it. Subclass it, if you need additional functionality.

    **Optional arguments:**

    ``fail_silently``
        If ``True``, errors when sending the email will be silently
        supressed (i.e., with no logging or reporting of any such
        errors. Default value is ``False``.

    ``form_class``
        The form to use. If not supplied, this will default to
        ``contact_form.forms.ContactForm``. If supplied, the form
        class must implement a method named ``save()`` which sends the
        email from the form; the form class must accept an
        ``HttpRequest`` as the keyword argument ``request`` to its
        constructor, and it must implement a method named ``save()``
        which sends the email and which accepts the keyword argument
        ``fail_silently``.

    ``success_url``
        The URL to redirect to after a successful submission. If not
        supplied, this will default to the URL pointed to by the named
        URL pattern ``contact_form_sent``.

    ``template_name``
        The template to use for rendering the contact form. If not
        supplied, defaults to
        :template:`contact_form/contact_form.html`.
    """

    template_name = 'contact_form/contact_form.html'
    form_class = ContactForm
    success_url = None
    fail_silently = False

    def get_form_kwargs(self):
        kwargs = super(ContactFormView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            self.form = self.form_class(data=request.POST, 
                                files=request.FILES,
                                request=request)
            if self.form.is_valid():
                self.form.save(fail_silently=self.fail_silently)

                # We set up success_url here, rather than as the default value for
                # the argument. Trying to do it as the argument's default would
                # mean evaluating the call to reverse() at the time this module is
                # first imported, which introduces a circular dependency: to
                # perform the reverse lookup we need access to
                # contact_form/urls.py, but contact_form/urls.py in turn imports
                # from this module.
               
                if self.success_url is None:
                    to, args, kwargs = self.form.get_success_redirect()
                    return redirect(to, *args, **kwargs)
                else:
                    return redirect(self.success_url)
        else:
            self.form = self.form_class(request=request)

        return super(ContactFormView, self).dispatch(request, *args, **kwargs)
