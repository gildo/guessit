#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GuessIt - A library for guessing information from filenames
# Copyright (c) 2013 Nicolas Wack <wackou@gmail.com>
# Copyright (c) 2013 Rémi Alvergnat <toilal.dev@gmail.com>
# Copyright (c) 2011 Ricard Marxer <ricardmp@gmail.com>
#
# GuessIt is free software; you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# GuessIt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function, unicode_literals

property_synonyms = {'Special Edition': ['Special'],
                     'Collector Edition': ['Collector'],
                     'Criterion Edition': ['Criterion']
                     }


def __revert_synonyms():
    reverse = {}

    for canonical, synonyms in property_synonyms.items():
        for synonym in synonyms:
            reverse[synonym.lower()] = canonical

    return reverse

reverse_synonyms = __revert_synonyms()


def get_synonym(string):
    return reverse_synonyms.get(string.lower(), string)
