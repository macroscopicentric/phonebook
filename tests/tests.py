import unittest
from nose.tools import eq_

import json

import phonebook.phonebook as phonebook

#to do: accept input from terminal

class TestBasicFunctions(unittest.TestCase):
    def tearDown(self):
        phonebook_dict = {'cosima niehaus': '289 470 8827',
            'beth march': '937 426 3323', 'beth childs': '559 393 0445',
            'alison hendrix': '710 342 9086', 'sarah manning': '305 883 2966',
            'katya obinger': '570 329 1984'}
        json.dump(phonebook_dict, open('testphonebook.pb', 'w'), indent=2)

    def test_lookup(self):
        eq_(phonebook.lookup('Beth', 'testphonebook.pb'),
            '''Beth Childs 559 393 0445\nBeth March 937 426 3323\n''')

    def test_add(self):
        name = 'Tony Sawicki'
        phone_number = '344 801 4521'
        eq_(phonebook.add_number(name, phone_number, 'testphonebook.pb'),
            'Tony Sawicki added.')

    def test_change(self):
        name = 'Cosima Niehaus'
        phone_number = '502 944 7810'
        eq_(phonebook.change_number(name, phone_number, 'testphonebook.pb'),
            'Cosima Niehaus changed.')

    def test_remove(self):
        eq_(phonebook.remove_number('Alison Hendrix', 'testphonebook.pb'),
            'Alison Hendrix removed.')

    def test_reverse_lookup(self):
        eq_(phonebook.reverse_lookup('559 393 0445', 'testphonebook.pb'),
            'Beth Childs 559 393 0445')

    def test_create(self):
        eq_(phonebook.create('newphonebook.pb'),
            'Created phonebook newphonebook.pb in the current directory.')

class TestErrors(unittest.TestCase):
    def test_lookup_error(self):
        eq_(phonebook.lookup('Beth', 'testphonebook1.pb'),
            'Error: That phonebook does not exist.')

    def test_reverse_lookup_error(self):
        eq_(phonebook.reverse_lookup('910 389 2634', 'testphonebook.pb'),
            'Error: that phone number does not exist.')

    def test_add_error(self):
        eq_(phonebook.add_number('Alison Hendrix', '827 479 1045',
            'testphonebook.pb'), 'Error: that name already exists.')

    def test_change_error(self):
        eq_(phonebook.change_number('Tony Sawicki', '344 801 4521',
            'testphonebook.pb'), 'Error: that name does not exist.')

    def test_remove_error(self):
        eq_(phonebook.remove_number('Tony Sawicki', 'testphonebook.pb'),
            'Error: that name does not exist.')

