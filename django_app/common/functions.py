import traceback
import random
import string

import sys
from django.core.mail import EmailMultiAlternatives
from math import sin, cos, sqrt, atan2, radians


def send_email(subject, content, to, content_type="text/plain"):
    """
    Envía un email con el contenido que se le designe.
    :param subject: Título del email.
    :param content: contenido o body del mensaje.
    :param content_type: tipo de contenido Ej. "text/plain"
    :param to: lista de usuarios a los que llegará el email.
    :return: True o False para confirmar el envío.
    """
    try:
        msg = EmailMultiAlternatives(subject=subject, body=content, to=to)
        if content_type == "text/html":
            msg.attach_alternative(content, "text/html")
        msg.send()
    except:
        message = format_sys_errors(sys, with_traceback=True)
        print(message)


def format_sys_errors(user_sys, with_traceback=False):
    if user_sys:
        etype, value, tb = user_sys.exc_info()
        tipo_error_name = etype.__name__
        error_args = value.args
        if with_traceback:
            mensaje = "{0} {1} {2}".format(
                tipo_error_name, error_args, traceback.extract_tb(tb))
        else:
            traceback.print_tb(tb)
            mensaje = "{0} {1}".format(tipo_error_name, error_args)
        return mensaje
    else:
        return ""
