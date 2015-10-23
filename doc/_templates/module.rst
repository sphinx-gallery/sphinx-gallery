{{ fullname }}
{{ underline }}

.. automodule:: {{ fullname }}

   {% block functions %}
   {% if functions %}

   Functions
   ---------

   {% for item in functions %}
   .. autofunction:: {{ item }}

   .. include:: {{fullname}}.{{item}}.examples

   .. raw:: html

	       <div style='clear:both'></div>
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block classes %}
   {% if classes %}

   Classes
   -------

   .. autosummary::
   {% for item in classes %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block exceptions %}
   {% if exceptions %}

   Exceptions
   ----------

   .. autosummary::
   {% for item in exceptions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}
