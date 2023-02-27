
from django.forms import ModelForm
from main_app.models import *

class BASIC_STRUCTURE_MF(ModelForm):


	class Meta:

		model=BASIC_STRUCTURE
		fields="__all__"

class FULL_CODE_MF(ModelForm):


	class Meta:

		model=FULL_CODE
		fields="__all__"

class RB_CATEGO_MF(ModelForm):


	class Meta:

		model=RB_CATEGO
		fields="__all__"

class RB_SUBC_MF(ModelForm):


	class Meta:

		model=RB_SUBC
		fields="__all__"

class RB_TYPE_MF(ModelForm):


	class Meta:

		model=RB_TYPE
		fields="__all__"

class C_CATEGO_MF(ModelForm):


	class Meta:

		model=C_CATEGO
		fields="__all__"

class C_SUBC_MF(ModelForm):


	class Meta:

		model=C_SUBC
		fields="__all__"

class C_TYPE_MF(ModelForm):


	class Meta:

		model=C_TYPE
		fields="__all__"

class COMPONENT_MF(ModelForm):


	class Meta:

		model=COMPONENT
		fields="__all__"

class ROBOT_MF(ModelForm):


	class Meta:

		model=ROBOT
		fields="__all__"
		exclude=['bot_code']

class CODE_MF(ModelForm):


	class Meta:

		model=CODE
		fields="__all__"

class BASIC_LIBRARY_MF(ModelForm):


	class Meta:

		model=BASIC_LIBRARY
		fields="__all__"

class BASIC_COMP_MF(ModelForm):


	class Meta:

		model=BASIC_COMP
		fields="__all__"

