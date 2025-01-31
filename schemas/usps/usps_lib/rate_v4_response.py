#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Sat May 29 15:46:59 2021 by generateDS.py version 2.38.6.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './usps_lib/rate_v4_response.py')
#
# Command line arguments:
#   ./schemas/RateV4Response.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./usps_lib/rate_v4_response.py" ./schemas/RateV4Response.xsd
#
# Current working directory (os.getcwd()):
#   usps
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class RateV4Response(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Package=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Package is None:
            self.Package = []
        else:
            self.Package = Package
        self.Package_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RateV4Response)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RateV4Response.subclass:
            return RateV4Response.subclass(*args_, **kwargs_)
        else:
            return RateV4Response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Package(self):
        return self.Package
    def set_Package(self, Package):
        self.Package = Package
    def add_Package(self, value):
        self.Package.append(value)
    def insert_Package_at(self, index, value):
        self.Package.insert(index, value)
    def replace_Package_at(self, index, value):
        self.Package[index] = value
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.Package or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RateV4Response', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RateV4Response')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RateV4Response':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RateV4Response')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RateV4Response', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RateV4Response'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RateV4Response', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Package_ in self.Package:
            namespaceprefix_ = self.Package_nsprefix_ + ':' if (UseCapturedNS_ and self.Package_nsprefix_) else ''
            Package_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Package', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Package':
            obj_ = PackageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Package', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Package'):
              self.add_Package(obj_.value)
            elif hasattr(self, 'set_Package'):
              self.set_Package(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class RateV4Response


class PackageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ID=None, Error=None, ZipOrigination=None, ZipDestination=None, Pounds=None, Ounces=None, FirstClassMailType=None, Container=None, Size=None, Width=None, Length=None, Height=None, Girth=None, Machinable=None, Zone=None, Postage=None, Restriction=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ID = _cast(None, ID)
        self.ID_nsprefix_ = None
        self.Error = Error
        self.Error_nsprefix_ = None
        self.ZipOrigination = ZipOrigination
        self.ZipOrigination_nsprefix_ = None
        self.ZipDestination = ZipDestination
        self.ZipDestination_nsprefix_ = None
        self.Pounds = Pounds
        self.Pounds_nsprefix_ = None
        self.Ounces = Ounces
        self.Ounces_nsprefix_ = None
        self.FirstClassMailType = FirstClassMailType
        self.FirstClassMailType_nsprefix_ = None
        self.Container = Container
        self.Container_nsprefix_ = None
        self.Size = Size
        self.Size_nsprefix_ = None
        self.Width = Width
        self.Width_nsprefix_ = None
        self.Length = Length
        self.Length_nsprefix_ = None
        self.Height = Height
        self.Height_nsprefix_ = None
        self.Girth = Girth
        self.Girth_nsprefix_ = None
        self.Machinable = Machinable
        self.Machinable_nsprefix_ = None
        self.Zone = Zone
        self.Zone_nsprefix_ = None
        if Postage is None:
            self.Postage = []
        else:
            self.Postage = Postage
        self.Postage_nsprefix_ = None
        self.Restriction = Restriction
        self.Restriction_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PackageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PackageType.subclass:
            return PackageType.subclass(*args_, **kwargs_)
        else:
            return PackageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Error(self):
        return self.Error
    def set_Error(self, Error):
        self.Error = Error
    def get_ZipOrigination(self):
        return self.ZipOrigination
    def set_ZipOrigination(self, ZipOrigination):
        self.ZipOrigination = ZipOrigination
    def get_ZipDestination(self):
        return self.ZipDestination
    def set_ZipDestination(self, ZipDestination):
        self.ZipDestination = ZipDestination
    def get_Pounds(self):
        return self.Pounds
    def set_Pounds(self, Pounds):
        self.Pounds = Pounds
    def get_Ounces(self):
        return self.Ounces
    def set_Ounces(self, Ounces):
        self.Ounces = Ounces
    def get_FirstClassMailType(self):
        return self.FirstClassMailType
    def set_FirstClassMailType(self, FirstClassMailType):
        self.FirstClassMailType = FirstClassMailType
    def get_Container(self):
        return self.Container
    def set_Container(self, Container):
        self.Container = Container
    def get_Size(self):
        return self.Size
    def set_Size(self, Size):
        self.Size = Size
    def get_Width(self):
        return self.Width
    def set_Width(self, Width):
        self.Width = Width
    def get_Length(self):
        return self.Length
    def set_Length(self, Length):
        self.Length = Length
    def get_Height(self):
        return self.Height
    def set_Height(self, Height):
        self.Height = Height
    def get_Girth(self):
        return self.Girth
    def set_Girth(self, Girth):
        self.Girth = Girth
    def get_Machinable(self):
        return self.Machinable
    def set_Machinable(self, Machinable):
        self.Machinable = Machinable
    def get_Zone(self):
        return self.Zone
    def set_Zone(self, Zone):
        self.Zone = Zone
    def get_Postage(self):
        return self.Postage
    def set_Postage(self, Postage):
        self.Postage = Postage
    def add_Postage(self, value):
        self.Postage.append(value)
    def insert_Postage_at(self, index, value):
        self.Postage.insert(index, value)
    def replace_Postage_at(self, index, value):
        self.Postage[index] = value
    def get_Restriction(self):
        return self.Restriction
    def set_Restriction(self, Restriction):
        self.Restriction = Restriction
    def get_ID(self):
        return self.ID
    def set_ID(self, ID):
        self.ID = ID
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.Error is not None or
            self.ZipOrigination is not None or
            self.ZipDestination is not None or
            self.Pounds is not None or
            self.Ounces is not None or
            self.FirstClassMailType is not None or
            self.Container is not None or
            self.Size is not None or
            self.Width is not None or
            self.Length is not None or
            self.Height is not None or
            self.Girth is not None or
            self.Machinable is not None or
            self.Zone is not None or
            self.Postage or
            self.Restriction is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PackageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PackageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PackageType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PackageType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PackageType'):
        if self.ID is not None and 'ID' not in already_processed:
            already_processed.add('ID')
            outfile.write(' ID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ID), input_name='ID')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackageType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Error is not None:
            namespaceprefix_ = self.Error_nsprefix_ + ':' if (UseCapturedNS_ and self.Error_nsprefix_) else ''
            self.Error.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Error', pretty_print=pretty_print)
        if self.ZipOrigination is not None:
            namespaceprefix_ = self.ZipOrigination_nsprefix_ + ':' if (UseCapturedNS_ and self.ZipOrigination_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sZipOrigination>%s</%sZipOrigination>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ZipOrigination), input_name='ZipOrigination')), namespaceprefix_ , eol_))
        if self.ZipDestination is not None:
            namespaceprefix_ = self.ZipDestination_nsprefix_ + ':' if (UseCapturedNS_ and self.ZipDestination_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sZipDestination>%s</%sZipDestination>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ZipDestination), input_name='ZipDestination')), namespaceprefix_ , eol_))
        if self.Pounds is not None:
            namespaceprefix_ = self.Pounds_nsprefix_ + ':' if (UseCapturedNS_ and self.Pounds_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPounds>%s</%sPounds>%s' % (namespaceprefix_ , self.gds_format_integer(self.Pounds, input_name='Pounds'), namespaceprefix_ , eol_))
        if self.Ounces is not None:
            namespaceprefix_ = self.Ounces_nsprefix_ + ':' if (UseCapturedNS_ and self.Ounces_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOunces>%s</%sOunces>%s' % (namespaceprefix_ , self.gds_format_decimal(self.Ounces, input_name='Ounces'), namespaceprefix_ , eol_))
        if self.FirstClassMailType is not None:
            namespaceprefix_ = self.FirstClassMailType_nsprefix_ + ':' if (UseCapturedNS_ and self.FirstClassMailType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFirstClassMailType>%s</%sFirstClassMailType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.FirstClassMailType), input_name='FirstClassMailType')), namespaceprefix_ , eol_))
        if self.Container is not None:
            namespaceprefix_ = self.Container_nsprefix_ + ':' if (UseCapturedNS_ and self.Container_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sContainer>%s</%sContainer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Container), input_name='Container')), namespaceprefix_ , eol_))
        if self.Size is not None:
            namespaceprefix_ = self.Size_nsprefix_ + ':' if (UseCapturedNS_ and self.Size_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSize>%s</%sSize>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Size), input_name='Size')), namespaceprefix_ , eol_))
        if self.Width is not None:
            namespaceprefix_ = self.Width_nsprefix_ + ':' if (UseCapturedNS_ and self.Width_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sWidth>%s</%sWidth>%s' % (namespaceprefix_ , self.gds_format_decimal(self.Width, input_name='Width'), namespaceprefix_ , eol_))
        if self.Length is not None:
            namespaceprefix_ = self.Length_nsprefix_ + ':' if (UseCapturedNS_ and self.Length_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLength>%s</%sLength>%s' % (namespaceprefix_ , self.gds_format_decimal(self.Length, input_name='Length'), namespaceprefix_ , eol_))
        if self.Height is not None:
            namespaceprefix_ = self.Height_nsprefix_ + ':' if (UseCapturedNS_ and self.Height_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHeight>%s</%sHeight>%s' % (namespaceprefix_ , self.gds_format_decimal(self.Height, input_name='Height'), namespaceprefix_ , eol_))
        if self.Girth is not None:
            namespaceprefix_ = self.Girth_nsprefix_ + ':' if (UseCapturedNS_ and self.Girth_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sGirth>%s</%sGirth>%s' % (namespaceprefix_ , self.gds_format_decimal(self.Girth, input_name='Girth'), namespaceprefix_ , eol_))
        if self.Machinable is not None:
            namespaceprefix_ = self.Machinable_nsprefix_ + ':' if (UseCapturedNS_ and self.Machinable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMachinable>%s</%sMachinable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Machinable), input_name='Machinable')), namespaceprefix_ , eol_))
        if self.Zone is not None:
            namespaceprefix_ = self.Zone_nsprefix_ + ':' if (UseCapturedNS_ and self.Zone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sZone>%s</%sZone>%s' % (namespaceprefix_ , self.gds_format_integer(self.Zone, input_name='Zone'), namespaceprefix_ , eol_))
        for Postage_ in self.Postage:
            namespaceprefix_ = self.Postage_nsprefix_ + ':' if (UseCapturedNS_ and self.Postage_nsprefix_) else ''
            Postage_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Postage', pretty_print=pretty_print)
        if self.Restriction is not None:
            namespaceprefix_ = self.Restriction_nsprefix_ + ':' if (UseCapturedNS_ and self.Restriction_nsprefix_) else ''
            self.Restriction.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Restriction', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ID', node)
        if value is not None and 'ID' not in already_processed:
            already_processed.add('ID')
            self.ID = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Error':
            obj_ = ErrorType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Error', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Error'):
              self.add_Error(obj_.value)
            elif hasattr(self, 'set_Error'):
              self.set_Error(obj_.value)
        elif nodeName_ == 'ZipOrigination' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'ZipOrigination')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'ZipOrigination')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'ZipOrigination', valuestr_)
            self.content_.append(obj_)
            self.ZipOrigination_nsprefix_ = child_.prefix
        elif nodeName_ == 'ZipDestination' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'ZipDestination')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'ZipDestination')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'ZipDestination', valuestr_)
            self.content_.append(obj_)
            self.ZipDestination_nsprefix_ = child_.prefix
        elif nodeName_ == 'Pounds' and child_.text is not None:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Pounds')
            ival_ = self.gds_validate_integer(ival_, node, 'Pounds')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeInteger, 'Pounds', ival_)
            self.content_.append(obj_)
            self.Pounds_nsprefix_ = child_.prefix
        elif nodeName_ == 'Ounces' and child_.text is not None:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Ounces')
            fval_ = self.gds_validate_decimal(fval_, node, 'Ounces')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeFloat, 'Ounces', fval_)
            self.content_.append(obj_)
            self.Ounces_nsprefix_ = child_.prefix
        elif nodeName_ == 'FirstClassMailType' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'FirstClassMailType')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'FirstClassMailType')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'FirstClassMailType', valuestr_)
            self.content_.append(obj_)
            self.FirstClassMailType_nsprefix_ = child_.prefix
        elif nodeName_ == 'Container' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'Container')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'Container')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'Container', valuestr_)
            self.content_.append(obj_)
            self.Container_nsprefix_ = child_.prefix
        elif nodeName_ == 'Size' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'Size')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'Size')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'Size', valuestr_)
            self.content_.append(obj_)
            self.Size_nsprefix_ = child_.prefix
        elif nodeName_ == 'Width' and child_.text is not None:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Width')
            fval_ = self.gds_validate_decimal(fval_, node, 'Width')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeFloat, 'Width', fval_)
            self.content_.append(obj_)
            self.Width_nsprefix_ = child_.prefix
        elif nodeName_ == 'Length' and child_.text is not None:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Length')
            fval_ = self.gds_validate_decimal(fval_, node, 'Length')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeFloat, 'Length', fval_)
            self.content_.append(obj_)
            self.Length_nsprefix_ = child_.prefix
        elif nodeName_ == 'Height' and child_.text is not None:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Height')
            fval_ = self.gds_validate_decimal(fval_, node, 'Height')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeFloat, 'Height', fval_)
            self.content_.append(obj_)
            self.Height_nsprefix_ = child_.prefix
        elif nodeName_ == 'Girth' and child_.text is not None:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Girth')
            fval_ = self.gds_validate_decimal(fval_, node, 'Girth')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeFloat, 'Girth', fval_)
            self.content_.append(obj_)
            self.Girth_nsprefix_ = child_.prefix
        elif nodeName_ == 'Machinable' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'Machinable')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'Machinable')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'Machinable', valuestr_)
            self.content_.append(obj_)
            self.Machinable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Zone' and child_.text is not None:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Zone')
            ival_ = self.gds_validate_integer(ival_, node, 'Zone')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeInteger, 'Zone', ival_)
            self.content_.append(obj_)
            self.Zone_nsprefix_ = child_.prefix
        elif nodeName_ == 'Postage':
            obj_ = PostageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Postage', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Postage'):
              self.add_Postage(obj_.value)
            elif hasattr(self, 'set_Postage'):
              self.set_Postage(obj_.value)
        elif nodeName_ == 'Restriction':
            obj_ = RestrictionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Restriction', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Restriction'):
              self.add_Restriction(obj_.value)
            elif hasattr(self, 'set_Restriction'):
              self.set_Restriction(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class PackageType


class ErrorType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Number=None, Source=None, Description=None, HelpFile=None, HelpContext=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        self.Source = Source
        self.Source_nsprefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
        self.HelpFile = HelpFile
        self.HelpFile_nsprefix_ = None
        self.HelpContext = HelpContext
        self.HelpContext_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ErrorType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ErrorType.subclass:
            return ErrorType.subclass(*args_, **kwargs_)
        else:
            return ErrorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_Source(self):
        return self.Source
    def set_Source(self, Source):
        self.Source = Source
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def get_HelpFile(self):
        return self.HelpFile
    def set_HelpFile(self, HelpFile):
        self.HelpFile = HelpFile
    def get_HelpContext(self):
        return self.HelpContext
    def set_HelpContext(self, HelpContext):
        self.HelpContext = HelpContext
    def hasContent_(self):
        if (
            self.Number is not None or
            self.Source is not None or
            self.Description is not None or
            self.HelpFile is not None or
            self.HelpContext is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ErrorType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ErrorType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ErrorType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ErrorType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ErrorType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ErrorType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ErrorType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        if self.Source is not None:
            namespaceprefix_ = self.Source_nsprefix_ + ':' if (UseCapturedNS_ and self.Source_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSource>%s</%sSource>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Source), input_name='Source')), namespaceprefix_ , eol_))
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
        if self.HelpFile is not None:
            namespaceprefix_ = self.HelpFile_nsprefix_ + ':' if (UseCapturedNS_ and self.HelpFile_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHelpFile>%s</%sHelpFile>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.HelpFile), input_name='HelpFile')), namespaceprefix_ , eol_))
        if self.HelpContext is not None:
            namespaceprefix_ = self.HelpContext_nsprefix_ + ':' if (UseCapturedNS_ and self.HelpContext_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHelpContext>%s</%sHelpContext>%s' % (namespaceprefix_ , self.gds_format_integer(self.HelpContext, input_name='HelpContext'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Number' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Number')
            ival_ = self.gds_validate_integer(ival_, node, 'Number')
            self.Number = ival_
            self.Number_nsprefix_ = child_.prefix
        elif nodeName_ == 'Source':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Source')
            value_ = self.gds_validate_string(value_, node, 'Source')
            self.Source = value_
            self.Source_nsprefix_ = child_.prefix
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
        elif nodeName_ == 'HelpFile':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'HelpFile')
            value_ = self.gds_validate_string(value_, node, 'HelpFile')
            self.HelpFile = value_
            self.HelpFile_nsprefix_ = child_.prefix
        elif nodeName_ == 'HelpContext' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'HelpContext')
            ival_ = self.gds_validate_integer(ival_, node, 'HelpContext')
            self.HelpContext = ival_
            self.HelpContext_nsprefix_ = child_.prefix
# end class ErrorType


class PostageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CLASSID=None, MailService=None, Rate=None, CommercialRate=None, CommercialPlusRate=None, CommitmentDate=None, CommitmentName=None, MaxDimensions=None, ServiceInformation=None, SpecialServices=None, Zone=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CLASSID = _cast(int, CLASSID)
        self.CLASSID_nsprefix_ = None
        self.MailService = MailService
        self.MailService_nsprefix_ = None
        self.Rate = Rate
        self.Rate_nsprefix_ = None
        self.CommercialRate = CommercialRate
        self.CommercialRate_nsprefix_ = None
        self.CommercialPlusRate = CommercialPlusRate
        self.CommercialPlusRate_nsprefix_ = None
        self.CommitmentDate = CommitmentDate
        self.CommitmentDate_nsprefix_ = None
        self.CommitmentName = CommitmentName
        self.CommitmentName_nsprefix_ = None
        self.MaxDimensions = MaxDimensions
        self.MaxDimensions_nsprefix_ = None
        self.ServiceInformation = ServiceInformation
        self.ServiceInformation_nsprefix_ = None
        self.SpecialServices = SpecialServices
        self.SpecialServices_nsprefix_ = None
        self.Zone = Zone
        self.Zone_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PostageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PostageType.subclass:
            return PostageType.subclass(*args_, **kwargs_)
        else:
            return PostageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MailService(self):
        return self.MailService
    def set_MailService(self, MailService):
        self.MailService = MailService
    def get_Rate(self):
        return self.Rate
    def set_Rate(self, Rate):
        self.Rate = Rate
    def get_CommercialRate(self):
        return self.CommercialRate
    def set_CommercialRate(self, CommercialRate):
        self.CommercialRate = CommercialRate
    def get_CommercialPlusRate(self):
        return self.CommercialPlusRate
    def set_CommercialPlusRate(self, CommercialPlusRate):
        self.CommercialPlusRate = CommercialPlusRate
    def get_CommitmentDate(self):
        return self.CommitmentDate
    def set_CommitmentDate(self, CommitmentDate):
        self.CommitmentDate = CommitmentDate
    def get_CommitmentName(self):
        return self.CommitmentName
    def set_CommitmentName(self, CommitmentName):
        self.CommitmentName = CommitmentName
    def get_MaxDimensions(self):
        return self.MaxDimensions
    def set_MaxDimensions(self, MaxDimensions):
        self.MaxDimensions = MaxDimensions
    def get_ServiceInformation(self):
        return self.ServiceInformation
    def set_ServiceInformation(self, ServiceInformation):
        self.ServiceInformation = ServiceInformation
    def get_SpecialServices(self):
        return self.SpecialServices
    def set_SpecialServices(self, SpecialServices):
        self.SpecialServices = SpecialServices
    def get_Zone(self):
        return self.Zone
    def set_Zone(self, Zone):
        self.Zone = Zone
    def get_CLASSID(self):
        return self.CLASSID
    def set_CLASSID(self, CLASSID):
        self.CLASSID = CLASSID
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.MailService is not None or
            self.Rate is not None or
            self.CommercialRate is not None or
            self.CommercialPlusRate is not None or
            self.CommitmentDate is not None or
            self.CommitmentName is not None or
            self.MaxDimensions is not None or
            self.ServiceInformation is not None or
            self.SpecialServices is not None or
            self.Zone is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PostageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PostageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PostageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PostageType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PostageType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PostageType'):
        if self.CLASSID is not None and 'CLASSID' not in already_processed:
            already_processed.add('CLASSID')
            outfile.write(' CLASSID="%s"' % self.gds_format_integer(self.CLASSID, input_name='CLASSID'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PostageType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.MailService is not None:
            namespaceprefix_ = self.MailService_nsprefix_ + ':' if (UseCapturedNS_ and self.MailService_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMailService>%s</%sMailService>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MailService), input_name='MailService')), namespaceprefix_ , eol_))
        if self.Rate is not None:
            namespaceprefix_ = self.Rate_nsprefix_ + ':' if (UseCapturedNS_ and self.Rate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRate>%s</%sRate>%s' % (namespaceprefix_ , self.gds_format_float(self.Rate, input_name='Rate'), namespaceprefix_ , eol_))
        if self.CommercialRate is not None:
            namespaceprefix_ = self.CommercialRate_nsprefix_ + ':' if (UseCapturedNS_ and self.CommercialRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCommercialRate>%s</%sCommercialRate>%s' % (namespaceprefix_ , self.gds_format_float(self.CommercialRate, input_name='CommercialRate'), namespaceprefix_ , eol_))
        if self.CommercialPlusRate is not None:
            namespaceprefix_ = self.CommercialPlusRate_nsprefix_ + ':' if (UseCapturedNS_ and self.CommercialPlusRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCommercialPlusRate>%s</%sCommercialPlusRate>%s' % (namespaceprefix_ , self.gds_format_float(self.CommercialPlusRate, input_name='CommercialPlusRate'), namespaceprefix_ , eol_))
        if self.CommitmentDate is not None:
            namespaceprefix_ = self.CommitmentDate_nsprefix_ + ':' if (UseCapturedNS_ and self.CommitmentDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCommitmentDate>%s</%sCommitmentDate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CommitmentDate), input_name='CommitmentDate')), namespaceprefix_ , eol_))
        if self.CommitmentName is not None:
            namespaceprefix_ = self.CommitmentName_nsprefix_ + ':' if (UseCapturedNS_ and self.CommitmentName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCommitmentName>%s</%sCommitmentName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CommitmentName), input_name='CommitmentName')), namespaceprefix_ , eol_))
        if self.MaxDimensions is not None:
            namespaceprefix_ = self.MaxDimensions_nsprefix_ + ':' if (UseCapturedNS_ and self.MaxDimensions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMaxDimensions>%s</%sMaxDimensions>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MaxDimensions), input_name='MaxDimensions')), namespaceprefix_ , eol_))
        if self.ServiceInformation is not None:
            namespaceprefix_ = self.ServiceInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceInformation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceInformation>%s</%sServiceInformation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ServiceInformation), input_name='ServiceInformation')), namespaceprefix_ , eol_))
        if self.SpecialServices is not None:
            namespaceprefix_ = self.SpecialServices_nsprefix_ + ':' if (UseCapturedNS_ and self.SpecialServices_nsprefix_) else ''
            self.SpecialServices.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SpecialServices', pretty_print=pretty_print)
        if self.Zone is not None:
            namespaceprefix_ = self.Zone_nsprefix_ + ':' if (UseCapturedNS_ and self.Zone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sZone>%s</%sZone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Zone), input_name='Zone')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('CLASSID', node)
        if value is not None and 'CLASSID' not in already_processed:
            already_processed.add('CLASSID')
            self.CLASSID = self.gds_parse_integer(value, node, 'CLASSID')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MailService' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'MailService')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'MailService')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'MailService', valuestr_)
            self.content_.append(obj_)
            self.MailService_nsprefix_ = child_.prefix
        elif nodeName_ == 'Rate' and child_.text is not None:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'Rate')
            fval_ = self.gds_validate_float(fval_, node, 'Rate')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeFloat, 'Rate', fval_)
            self.content_.append(obj_)
            self.Rate_nsprefix_ = child_.prefix
        elif nodeName_ == 'CommercialRate' and child_.text is not None:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'CommercialRate')
            fval_ = self.gds_validate_float(fval_, node, 'CommercialRate')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeFloat, 'CommercialRate', fval_)
            self.content_.append(obj_)
            self.CommercialRate_nsprefix_ = child_.prefix
        elif nodeName_ == 'CommercialPlusRate' and child_.text is not None:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'CommercialPlusRate')
            fval_ = self.gds_validate_float(fval_, node, 'CommercialPlusRate')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeFloat, 'CommercialPlusRate', fval_)
            self.content_.append(obj_)
            self.CommercialPlusRate_nsprefix_ = child_.prefix
        elif nodeName_ == 'CommitmentDate' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'CommitmentDate')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'CommitmentDate')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'CommitmentDate', valuestr_)
            self.content_.append(obj_)
            self.CommitmentDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'CommitmentName' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'CommitmentName')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'CommitmentName')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'CommitmentName', valuestr_)
            self.content_.append(obj_)
            self.CommitmentName_nsprefix_ = child_.prefix
        elif nodeName_ == 'MaxDimensions' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'MaxDimensions')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'MaxDimensions')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'MaxDimensions', valuestr_)
            self.content_.append(obj_)
            self.MaxDimensions_nsprefix_ = child_.prefix
        elif nodeName_ == 'ServiceInformation' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'ServiceInformation')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'ServiceInformation')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'ServiceInformation', valuestr_)
            self.content_.append(obj_)
            self.ServiceInformation_nsprefix_ = child_.prefix
        elif nodeName_ == 'SpecialServices':
            obj_ = SpecialServicesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'SpecialServices', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_SpecialServices'):
              self.add_SpecialServices(obj_.value)
            elif hasattr(self, 'set_SpecialServices'):
              self.set_SpecialServices(obj_.value)
        elif nodeName_ == 'Zone' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'Zone')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'Zone')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'Zone', valuestr_)
            self.content_.append(obj_)
            self.Zone_nsprefix_ = child_.prefix
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class PostageType


class SpecialServicesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SpecialService=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if SpecialService is None:
            self.SpecialService = []
        else:
            self.SpecialService = SpecialService
        self.SpecialService_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SpecialServicesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SpecialServicesType.subclass:
            return SpecialServicesType.subclass(*args_, **kwargs_)
        else:
            return SpecialServicesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SpecialService(self):
        return self.SpecialService
    def set_SpecialService(self, SpecialService):
        self.SpecialService = SpecialService
    def add_SpecialService(self, value):
        self.SpecialService.append(value)
    def insert_SpecialService_at(self, index, value):
        self.SpecialService.insert(index, value)
    def replace_SpecialService_at(self, index, value):
        self.SpecialService[index] = value
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.SpecialService or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SpecialServicesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SpecialServicesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SpecialServicesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SpecialServicesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SpecialServicesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SpecialServicesType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SpecialServicesType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SpecialService_ in self.SpecialService:
            namespaceprefix_ = self.SpecialService_nsprefix_ + ':' if (UseCapturedNS_ and self.SpecialService_nsprefix_) else ''
            SpecialService_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SpecialService', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SpecialService':
            obj_ = SpecialServiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'SpecialService', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_SpecialService'):
              self.add_SpecialService(obj_.value)
            elif hasattr(self, 'set_SpecialService'):
              self.set_SpecialService(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class SpecialServicesType


class SpecialServiceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceID=None, ServiceName=None, Available=None, AvailableOnline=None, AvailableCPP=None, Price=None, PriceOnline=None, PriceCPP=None, DeclaredValueRequired=None, DueSenderRequired=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ServiceID = ServiceID
        self.ServiceID_nsprefix_ = None
        self.ServiceName = ServiceName
        self.ServiceName_nsprefix_ = None
        self.Available = Available
        self.Available_nsprefix_ = None
        self.AvailableOnline = AvailableOnline
        self.AvailableOnline_nsprefix_ = None
        self.AvailableCPP = AvailableCPP
        self.AvailableCPP_nsprefix_ = None
        self.Price = Price
        self.Price_nsprefix_ = None
        self.PriceOnline = PriceOnline
        self.PriceOnline_nsprefix_ = None
        self.PriceCPP = PriceCPP
        self.PriceCPP_nsprefix_ = None
        self.DeclaredValueRequired = DeclaredValueRequired
        self.DeclaredValueRequired_nsprefix_ = None
        self.DueSenderRequired = DueSenderRequired
        self.DueSenderRequired_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SpecialServiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SpecialServiceType.subclass:
            return SpecialServiceType.subclass(*args_, **kwargs_)
        else:
            return SpecialServiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceID(self):
        return self.ServiceID
    def set_ServiceID(self, ServiceID):
        self.ServiceID = ServiceID
    def get_ServiceName(self):
        return self.ServiceName
    def set_ServiceName(self, ServiceName):
        self.ServiceName = ServiceName
    def get_Available(self):
        return self.Available
    def set_Available(self, Available):
        self.Available = Available
    def get_AvailableOnline(self):
        return self.AvailableOnline
    def set_AvailableOnline(self, AvailableOnline):
        self.AvailableOnline = AvailableOnline
    def get_AvailableCPP(self):
        return self.AvailableCPP
    def set_AvailableCPP(self, AvailableCPP):
        self.AvailableCPP = AvailableCPP
    def get_Price(self):
        return self.Price
    def set_Price(self, Price):
        self.Price = Price
    def get_PriceOnline(self):
        return self.PriceOnline
    def set_PriceOnline(self, PriceOnline):
        self.PriceOnline = PriceOnline
    def get_PriceCPP(self):
        return self.PriceCPP
    def set_PriceCPP(self, PriceCPP):
        self.PriceCPP = PriceCPP
    def get_DeclaredValueRequired(self):
        return self.DeclaredValueRequired
    def set_DeclaredValueRequired(self, DeclaredValueRequired):
        self.DeclaredValueRequired = DeclaredValueRequired
    def get_DueSenderRequired(self):
        return self.DueSenderRequired
    def set_DueSenderRequired(self, DueSenderRequired):
        self.DueSenderRequired = DueSenderRequired
    def hasContent_(self):
        if (
            self.ServiceID is not None or
            self.ServiceName is not None or
            self.Available is not None or
            self.AvailableOnline is not None or
            self.AvailableCPP is not None or
            self.Price is not None or
            self.PriceOnline is not None or
            self.PriceCPP is not None or
            self.DeclaredValueRequired is not None or
            self.DueSenderRequired is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SpecialServiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SpecialServiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SpecialServiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SpecialServiceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SpecialServiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SpecialServiceType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SpecialServiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceID is not None:
            namespaceprefix_ = self.ServiceID_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceID>%s</%sServiceID>%s' % (namespaceprefix_ , self.gds_format_integer(self.ServiceID, input_name='ServiceID'), namespaceprefix_ , eol_))
        if self.ServiceName is not None:
            namespaceprefix_ = self.ServiceName_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceName>%s</%sServiceName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ServiceName), input_name='ServiceName')), namespaceprefix_ , eol_))
        if self.Available is not None:
            namespaceprefix_ = self.Available_nsprefix_ + ':' if (UseCapturedNS_ and self.Available_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAvailable>%s</%sAvailable>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Available, input_name='Available'), namespaceprefix_ , eol_))
        if self.AvailableOnline is not None:
            namespaceprefix_ = self.AvailableOnline_nsprefix_ + ':' if (UseCapturedNS_ and self.AvailableOnline_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAvailableOnline>%s</%sAvailableOnline>%s' % (namespaceprefix_ , self.gds_format_boolean(self.AvailableOnline, input_name='AvailableOnline'), namespaceprefix_ , eol_))
        if self.AvailableCPP is not None:
            namespaceprefix_ = self.AvailableCPP_nsprefix_ + ':' if (UseCapturedNS_ and self.AvailableCPP_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAvailableCPP>%s</%sAvailableCPP>%s' % (namespaceprefix_ , self.gds_format_boolean(self.AvailableCPP, input_name='AvailableCPP'), namespaceprefix_ , eol_))
        if self.Price is not None:
            namespaceprefix_ = self.Price_nsprefix_ + ':' if (UseCapturedNS_ and self.Price_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPrice>%s</%sPrice>%s' % (namespaceprefix_ , self.gds_format_float(self.Price, input_name='Price'), namespaceprefix_ , eol_))
        if self.PriceOnline is not None:
            namespaceprefix_ = self.PriceOnline_nsprefix_ + ':' if (UseCapturedNS_ and self.PriceOnline_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPriceOnline>%s</%sPriceOnline>%s' % (namespaceprefix_ , self.gds_format_float(self.PriceOnline, input_name='PriceOnline'), namespaceprefix_ , eol_))
        if self.PriceCPP is not None:
            namespaceprefix_ = self.PriceCPP_nsprefix_ + ':' if (UseCapturedNS_ and self.PriceCPP_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPriceCPP>%s</%sPriceCPP>%s' % (namespaceprefix_ , self.gds_format_float(self.PriceCPP, input_name='PriceCPP'), namespaceprefix_ , eol_))
        if self.DeclaredValueRequired is not None:
            namespaceprefix_ = self.DeclaredValueRequired_nsprefix_ + ':' if (UseCapturedNS_ and self.DeclaredValueRequired_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDeclaredValueRequired>%s</%sDeclaredValueRequired>%s' % (namespaceprefix_ , self.gds_format_boolean(self.DeclaredValueRequired, input_name='DeclaredValueRequired'), namespaceprefix_ , eol_))
        if self.DueSenderRequired is not None:
            namespaceprefix_ = self.DueSenderRequired_nsprefix_ + ':' if (UseCapturedNS_ and self.DueSenderRequired_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDueSenderRequired>%s</%sDueSenderRequired>%s' % (namespaceprefix_ , self.gds_format_boolean(self.DueSenderRequired, input_name='DueSenderRequired'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ServiceID')
            ival_ = self.gds_validate_integer(ival_, node, 'ServiceID')
            self.ServiceID = ival_
            self.ServiceID_nsprefix_ = child_.prefix
        elif nodeName_ == 'ServiceName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ServiceName')
            value_ = self.gds_validate_string(value_, node, 'ServiceName')
            self.ServiceName = value_
            self.ServiceName_nsprefix_ = child_.prefix
        elif nodeName_ == 'Available':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Available')
            ival_ = self.gds_validate_boolean(ival_, node, 'Available')
            self.Available = ival_
            self.Available_nsprefix_ = child_.prefix
        elif nodeName_ == 'AvailableOnline':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'AvailableOnline')
            ival_ = self.gds_validate_boolean(ival_, node, 'AvailableOnline')
            self.AvailableOnline = ival_
            self.AvailableOnline_nsprefix_ = child_.prefix
        elif nodeName_ == 'AvailableCPP':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'AvailableCPP')
            ival_ = self.gds_validate_boolean(ival_, node, 'AvailableCPP')
            self.AvailableCPP = ival_
            self.AvailableCPP_nsprefix_ = child_.prefix
        elif nodeName_ == 'Price' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'Price')
            fval_ = self.gds_validate_float(fval_, node, 'Price')
            self.Price = fval_
            self.Price_nsprefix_ = child_.prefix
        elif nodeName_ == 'PriceOnline' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'PriceOnline')
            fval_ = self.gds_validate_float(fval_, node, 'PriceOnline')
            self.PriceOnline = fval_
            self.PriceOnline_nsprefix_ = child_.prefix
        elif nodeName_ == 'PriceCPP' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'PriceCPP')
            fval_ = self.gds_validate_float(fval_, node, 'PriceCPP')
            self.PriceCPP = fval_
            self.PriceCPP_nsprefix_ = child_.prefix
        elif nodeName_ == 'DeclaredValueRequired':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'DeclaredValueRequired')
            ival_ = self.gds_validate_boolean(ival_, node, 'DeclaredValueRequired')
            self.DeclaredValueRequired = ival_
            self.DeclaredValueRequired_nsprefix_ = child_.prefix
        elif nodeName_ == 'DueSenderRequired':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'DueSenderRequired')
            ival_ = self.gds_validate_boolean(ival_, node, 'DueSenderRequired')
            self.DueSenderRequired = ival_
            self.DueSenderRequired_nsprefix_ = child_.prefix
# end class SpecialServiceType


class RestrictionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Restrictions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Restrictions = Restrictions
        self.Restrictions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RestrictionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RestrictionType.subclass:
            return RestrictionType.subclass(*args_, **kwargs_)
        else:
            return RestrictionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Restrictions(self):
        return self.Restrictions
    def set_Restrictions(self, Restrictions):
        self.Restrictions = Restrictions
    def hasContent_(self):
        if (
            self.Restrictions is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RestrictionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RestrictionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RestrictionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RestrictionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RestrictionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RestrictionType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RestrictionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Restrictions is not None:
            namespaceprefix_ = self.Restrictions_nsprefix_ + ':' if (UseCapturedNS_ and self.Restrictions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRestrictions>%s</%sRestrictions>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Restrictions), input_name='Restrictions')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Restrictions':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Restrictions')
            value_ = self.gds_validate_string(value_, node, 'Restrictions')
            self.Restrictions = value_
            self.Restrictions_nsprefix_ = child_.prefix
# end class RestrictionType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RateV4Response'
        rootClass = RateV4Response
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RateV4Response'
        rootClass = RateV4Response
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RateV4Response'
        rootClass = RateV4Response
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RateV4Response'
        rootClass = RateV4Response
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from rate_v4_response import *\n\n')
        sys.stdout.write('import rate_v4_response as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {}

__all__ = [
    "ErrorType",
    "PackageType",
    "PostageType",
    "RateV4Response",
    "RestrictionType",
    "SpecialServiceType",
    "SpecialServicesType"
]
