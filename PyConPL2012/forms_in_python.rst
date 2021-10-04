==========================================================
Forms in python - problems and my proposal of solving them
==========================================================

* By Szymon Pyżalski

    * STX Next Python Experts
    * https://github.com/zefciu/Forms-in-python

Talk Description
=================

My lecture would consist of two parts. First I would like to discuss what can a developer expect from a form library. Secondly I will show a design of one that would address all these problems.

Introduction
============

The basis of reviews:

Why are they important?
-----------------------

Forms are ubiquitous across all Python frameworks

* Python is a strongly typed language so we have to handle input properly
* Closest to the user 

    * What they see most
    * This is where they tend to see our mistakes
    
* Our first line of defense against security against CSRF and other attack methods.
* Boilerplate and repetition removal

Scope of Features
-----------------------

All form libraries need to have the following components:

* User input handling

    * Type coercion
    * Validation
    
* Widget generation
* Data schema reflection

    * Critical boilerplate reduction
    * Try not to define both data and form schema
    
Challenges
-----------------------

* Flexible but not full of feature creep

    * Easy to grow too big
    * but you can't make the project unmanageable
    
* Allow reflection but don't bind user's hands

    * If you can't modify the reflection then the form library quickly becomes useless on real projects

* Portable but allows developers to use specific features

    * If coupled too tightly then it's hard to move to other projects
    * If coupled too loosely then API can suffer.
    
FormEncode
===========

* By Ian Book
* Minimalist: only validation, coercion, html-filling
* Was recommended by Pylons book
* **Problem**: No schema reflection

Django Forms
=============

* Second attempt
* Plays best in the Django framework
* **Problem**: Hard to create new widgets

.. code-block:: python

    from django.forms import ModelForm, Textarea

    class AuthorForm(ModelForm):
        class Meta:
            model = Author
            fields = ('name', 'title', 'birth_date')
            widgets = {
                'name': Textarea(attrs={'cols': 80, 'rows': 20}),
            }
            
Sprox
======

* Combines FormEncode and ToscaWidgets
* Extendable and easy to create new widgets
* **Problem**: unpleasant API

.. code-block:: python

    from sprox.formbase import AddRecordForm
    from formencode import Schema
    from formencode.validators import FieldsMatch
    from tw.forms import PasswordField, TextField

    form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                             'verify_password',
                                                             messages={'invalidNoMatch':
                                                             'Passwords do not match'}),))
    class RegistrationForm(AddRecordForm):
        __model__ = User
        __require_fields__     = ['password', 'user_name', 'email_address']
        __omit_fields__        = ['_password']
        __field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
        __base_validator__     = form_validator
        email_address          = TextField
        display_name           = TextField
        verify_password        = PasswordField('verify_password')

    registration_form = RegistrationForm(DBSession)

FormAlchemy
===========

* Built on idea of shcema reflection
* Generates forms and tables
* Type coercion 

.. code-block:: python

    fs = FieldSet(User)
    fs.append(Field('repeat_password').label('Repeat password'))

    def password_match(value, field):
        if value != field.parent.password.value:
            raise ValidationError('Passwords do not match')

    
Formish and Deform
====================

* deform is a fork of formish
* don't do reflection
* Strong seperation between schema and form
* Schema can be used for other data-parsing formats

.. code-block:: python

    class Schema(colander.Schema):
        password = colander.SchemaNode(
            colander.String(),
            validator=colander.Length(min=5),
            widget=deform.widget.CheckedPasswordWidget(size=20),
            description='Type your password and confirm it')
    schema = Schema()
    form = deform.Form(schema, buttons=('submit',)
    
Anthrax
========

https://github.com/zefciu/Anthrax

.. note:: The name comes from `classic literature`, where Galahad visits Castle Anthrax and has his purity threatened.

His own forms library. Pre-alpha but it looks interesting. 

* Highly modular. If you create a dependency, create a module
* 4 layers

    * fields
    * widgets
    * views
    * templates
    
* building blocks

    * forms: A collection of subcontainers and fields
    * Field: Knows how to validate and coerce a particular data type
    * Widget: a suggestion about presentation
    * Validator: Works on a form or container, ad-hoc or generic
    * Front-end: A complete system to render the form in forms like HTML, Dojo flavored HTML, Angular flavored HTML, XML, etc
    * View: Front end dependent object
    * Template: Let you define the output in a flexible way
    
* Building block relations

    * A form has fields. It can be rendered into a front end
    * A field has a list of widgets that are called depending on the format requested
    * A front-end handles some widgets by assigning views to render them.

.. code-block:: python

    class RegisterForm(Form):
        __validators__ = [('equals', 'password', 'repeat_password')]
        __reflect__ = ('eplasty', User)
        __frontend__ = 'dojo'
        login = {'label': 'Login'}
        hash = salt = None
        password = TextField(widgets=[PasswordInput], label='Hasło')
        repeat_password = TextField(widgets=[PasswordInput], label='Powtórz hasło')
        ok = HttpSubmit()
        
My thoughts on it:

    * I like the seperation of layers. 
    * Like the way widgets are a list attached to a field, not just as a single widget per field
    * I don't like the ``__<SOMETHING>__`` syntax. He likes them so we'll agree to disagree. ;-)
