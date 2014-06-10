# Copyright 2012 Beixinyuan(Nanjing), All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


__author__ = 'tangjun'
__date__ = '2012-01-31'
__version__ = 'v2.0.2'

from django.conf import settings

if settings.DEBUG:
    __log__ = '2012-01-24 v2.0.1 create'\
              'v2.0.2 add X_http_methodoverride_middleware'

import logging
LOG = logging.getLogger(__name__)

def creeper_prcessor(request):
    context = {
        "DEBUG": getattr(settings, "DEBUG", False),
        "AJAX_HOST_STATUS_TIME": getattr(settings,'AJAX_HOST_STATUS_TIME',30000),
        "INTERNAL_VERSION": getattr(settings,"INTERNAL_VERSION","unknown"),
        "PRODUCT_VERSION": getattr(settings,"PRODUCT_VERSION","unknown")
    }
    return context