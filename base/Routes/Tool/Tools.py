import openai
from ...models import Faculty_details
from django.contrib.auth.models import User


def get_user_mail(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(mail=usr_obj.username)
    return faculty_details.mail

def get_user_name(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(mail=usr_obj.username)
    return faculty_details.user_name
def get_user_obj(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(mail=usr_obj.username)
    return faculty_details
def get_user_role(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(mail=usr_obj.username)
    if faculty_details.role.role == 1:
        return "Admin"
    elif faculty_details.role.role == 2:
        return "Hod"
    elif faculty_details.role.role == 3:
        return "staff"
    elif faculty_details.role.role == 4:
        return "Student"
def remove_space(string):
  out = ""
  for i in string:
    if i != " ":
      out = out +  i
  return out

def gpt(queary):
    openai.api_key = "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"

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=queary,
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
    )
    return response.choices[0].get("text")
