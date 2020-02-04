#!/usr/bin/env python

# Copyright (C) 2020 by eHealth Africa : http://www.eHealthAfrica.org
#
# See the NOTICE file distributed with this work for additional information
# regarding copyright ownership.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


import enum

from firebase_admin.db import reference as realtime
from firebase_admin.firestore import client as cfs


class MessageHandlingException(Exception):
    # A simple way to handle the variety of expected misbehaviors in message sync
    # Between Aether and Firebase
    pass


class SyncMode(enum.Enum):
    SYNC = 1        # Firebase  <->  Aether
    FORWARD = 2     # Firebase   ->  Aether
    CONSUME = 3     # Firebase  <-   Aether
    NONE = 4        # Firebase   |   Aether


class RTDB(object):

    def __init__(self, app):
        self.app = app

    def path(self, path):
        return realtime(path, app=self.app)


def Firestore(app):
    return cfs(app)
