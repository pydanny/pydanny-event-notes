========================
Customizing Django Admin
========================

Peter Baumgartner and Michael Trythall

User Experience
===============

Problems with the Admin as a User Experience tool
-------------------------------------------------

 * UI is the gateway to application log
 * Users remember bad experiences, associate them with **you** and the admin
 * Good experiences - Happy Customers - Profit!
 * No dashboard, statistics, or recent activity
 * no actions or modules highlighted or given priority
 * No assistance/help for beginner users
 * Impact fromc hanges is not always clear
 * Disconnect from external systems.
 * Doesn't fit mental models
 * Apps are not organized by context
 * little or no navigation outside of breadcrumbs
 * Doesn't follow workflow
 
Missing features of the admin tool
----------------------------------

 * Content and asset management tools, e.g. WYSIWYG, image manipulation
 * Error recovery (undo)
 * Export/Import with certain tyoes
 * Inline help systems
 * Cross model search

Poor display for complex models
-------------------------------

 * Way too many fields on complex models
 * Try to limit your fields
 
Customizing the Experience
==========================

ModelAdminMedia
---------------
 
   * js
 
     * JQuery
     * AJAX
     * Fancy inlines
     * Inject HTML
   
   * CSS
 
     * colors
     * layout


Custom templates
-----------------

(base.html, change_form.html, etc)
 
Model admin / Model Form hacking
--------------------------------
 
   * list_editable
   * row level permissions
   
ModelForms
----------

Use a model form and tell the Admin class to use ModelForms.
Not well documented - UNNACCEPTABLE!