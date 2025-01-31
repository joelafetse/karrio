#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Sat May 29 15:46:59 2021 by generateDS.py version 2.38.6.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './usps_lib/rate_v4_request.py')
#
# Command line arguments:
#   ./schemas/RateV4Request.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./usps_lib/rate_v4_request.py" ./schemas/RateV4Request.xsd
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


class RateV4Request(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, USERID=None, Revision=None, Package=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.USERID = _cast(None, USERID)
        self.USERID_nsprefix_ = None
        self.Revision = Revision
        self.Revision_nsprefix_ = None
        if Package is None:
            self.Package = []
        else:
            self.Package = Package
        self.Package_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RateV4Request)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RateV4Request.subclass:
            return RateV4Request.subclass(*args_, **kwargs_)
        else:
            return RateV4Request(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Revision(self):
        return self.Revision
    def set_Revision(self, Revision):
        self.Revision = Revision
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
    def get_USERID(self):
        return self.USERID
    def set_USERID(self, USERID):
        self.USERID = USERID
    def hasContent_(self):
        if (
            self.Revision is not None or
            self.Package
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RateV4Request', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RateV4Request')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RateV4Request':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RateV4Request')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RateV4Request', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RateV4Request'):
        if self.USERID is not None and 'USERID' not in already_processed:
            already_processed.add('USERID')
            outfile.write(' USERID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.USERID), input_name='USERID')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RateV4Request', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Revision is not None:
            namespaceprefix_ = self.Revision_nsprefix_ + ':' if (UseCapturedNS_ and self.Revision_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRevision>%s</%sRevision>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Revision), input_name='Revision')), namespaceprefix_ , eol_))
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
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('USERID', node)
        if value is not None and 'USERID' not in already_processed:
            already_processed.add('USERID')
            self.USERID = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Revision':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Revision')
            value_ = self.gds_validate_string(value_, node, 'Revision')
            self.Revision = value_
            self.Revision_nsprefix_ = child_.prefix
        elif nodeName_ == 'Package':
            obj_ = PackageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Package.append(obj_)
            obj_.original_tagname_ = 'Package'
# end class RateV4Request


class PackageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ID=None, Service=None, FirstClassMailType=None, ZipOrigination=None, ZipDestination=None, Pounds=None, Ounces=None, Container=None, Size=None, Width=None, Length=None, Height=None, Girth=None, Value=None, AmountToCollect=None, SpecialServices=None, Content=None, GroundOnly=None, SortBy=None, Machinable=None, ReturnLocations=None, ReturnServiceInfo=None, DropOffTime=None, ShipDate=None, ReturnDimensionalWeight=None, TrackingRetentionPeriod=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ID = _cast(None, ID)
        self.ID_nsprefix_ = None
        self.Service = Service
        self.Service_nsprefix_ = None
        self.FirstClassMailType = FirstClassMailType
        self.FirstClassMailType_nsprefix_ = None
        self.ZipOrigination = ZipOrigination
        self.ZipOrigination_nsprefix_ = None
        self.ZipDestination = ZipDestination
        self.ZipDestination_nsprefix_ = None
        self.Pounds = Pounds
        self.validate_PoundsType(self.Pounds)
        self.Pounds_nsprefix_ = None
        self.Ounces = Ounces
        self.validate_OuncesType(self.Ounces)
        self.Ounces_nsprefix_ = None
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
        self.Value = Value
        self.Value_nsprefix_ = None
        self.AmountToCollect = AmountToCollect
        self.AmountToCollect_nsprefix_ = None
        self.SpecialServices = SpecialServices
        self.SpecialServices_nsprefix_ = None
        self.Content = Content
        self.Content_nsprefix_ = None
        self.GroundOnly = GroundOnly
        self.GroundOnly_nsprefix_ = None
        self.SortBy = SortBy
        self.SortBy_nsprefix_ = None
        self.Machinable = Machinable
        self.Machinable_nsprefix_ = None
        self.ReturnLocations = ReturnLocations
        self.ReturnLocations_nsprefix_ = None
        self.ReturnServiceInfo = ReturnServiceInfo
        self.ReturnServiceInfo_nsprefix_ = None
        self.DropOffTime = DropOffTime
        self.DropOffTime_nsprefix_ = None
        self.ShipDate = ShipDate
        self.ShipDate_nsprefix_ = None
        self.ReturnDimensionalWeight = ReturnDimensionalWeight
        self.ReturnDimensionalWeight_nsprefix_ = None
        self.TrackingRetentionPeriod = TrackingRetentionPeriod
        self.TrackingRetentionPeriod_nsprefix_ = None
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
    def get_Service(self):
        return self.Service
    def set_Service(self, Service):
        self.Service = Service
    def get_FirstClassMailType(self):
        return self.FirstClassMailType
    def set_FirstClassMailType(self, FirstClassMailType):
        self.FirstClassMailType = FirstClassMailType
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
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_AmountToCollect(self):
        return self.AmountToCollect
    def set_AmountToCollect(self, AmountToCollect):
        self.AmountToCollect = AmountToCollect
    def get_SpecialServices(self):
        return self.SpecialServices
    def set_SpecialServices(self, SpecialServices):
        self.SpecialServices = SpecialServices
    def get_Content(self):
        return self.Content
    def set_Content(self, Content):
        self.Content = Content
    def get_GroundOnly(self):
        return self.GroundOnly
    def set_GroundOnly(self, GroundOnly):
        self.GroundOnly = GroundOnly
    def get_SortBy(self):
        return self.SortBy
    def set_SortBy(self, SortBy):
        self.SortBy = SortBy
    def get_Machinable(self):
        return self.Machinable
    def set_Machinable(self, Machinable):
        self.Machinable = Machinable
    def get_ReturnLocations(self):
        return self.ReturnLocations
    def set_ReturnLocations(self, ReturnLocations):
        self.ReturnLocations = ReturnLocations
    def get_ReturnServiceInfo(self):
        return self.ReturnServiceInfo
    def set_ReturnServiceInfo(self, ReturnServiceInfo):
        self.ReturnServiceInfo = ReturnServiceInfo
    def get_DropOffTime(self):
        return self.DropOffTime
    def set_DropOffTime(self, DropOffTime):
        self.DropOffTime = DropOffTime
    def get_ShipDate(self):
        return self.ShipDate
    def set_ShipDate(self, ShipDate):
        self.ShipDate = ShipDate
    def get_ReturnDimensionalWeight(self):
        return self.ReturnDimensionalWeight
    def set_ReturnDimensionalWeight(self, ReturnDimensionalWeight):
        self.ReturnDimensionalWeight = ReturnDimensionalWeight
    def get_TrackingRetentionPeriod(self):
        return self.TrackingRetentionPeriod
    def set_TrackingRetentionPeriod(self, TrackingRetentionPeriod):
        self.TrackingRetentionPeriod = TrackingRetentionPeriod
    def get_ID(self):
        return self.ID
    def set_ID(self, ID):
        self.ID = ID
    def validate_PoundsType(self, value):
        result = True
        # Validate type PoundsType, a restriction on xs:integer.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on PoundsType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 70:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on PoundsType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_OuncesType(self, value):
        result = True
        # Validate type OuncesType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on OuncesType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1120.0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on OuncesType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Service is not None or
            self.FirstClassMailType is not None or
            self.ZipOrigination is not None or
            self.ZipDestination is not None or
            self.Pounds is not None or
            self.Ounces is not None or
            self.Container is not None or
            self.Size is not None or
            self.Width is not None or
            self.Length is not None or
            self.Height is not None or
            self.Girth is not None or
            self.Value is not None or
            self.AmountToCollect is not None or
            self.SpecialServices is not None or
            self.Content is not None or
            self.GroundOnly is not None or
            self.SortBy is not None or
            self.Machinable is not None or
            self.ReturnLocations is not None or
            self.ReturnServiceInfo is not None or
            self.DropOffTime is not None or
            self.ShipDate is not None or
            self.ReturnDimensionalWeight is not None or
            self.TrackingRetentionPeriod is not None
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
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Service is not None:
            namespaceprefix_ = self.Service_nsprefix_ + ':' if (UseCapturedNS_ and self.Service_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sService>%s</%sService>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Service), input_name='Service')), namespaceprefix_ , eol_))
        if self.FirstClassMailType is not None:
            namespaceprefix_ = self.FirstClassMailType_nsprefix_ + ':' if (UseCapturedNS_ and self.FirstClassMailType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFirstClassMailType>%s</%sFirstClassMailType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.FirstClassMailType), input_name='FirstClassMailType')), namespaceprefix_ , eol_))
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
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
        if self.AmountToCollect is not None:
            namespaceprefix_ = self.AmountToCollect_nsprefix_ + ':' if (UseCapturedNS_ and self.AmountToCollect_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAmountToCollect>%s</%sAmountToCollect>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AmountToCollect), input_name='AmountToCollect')), namespaceprefix_ , eol_))
        if self.SpecialServices is not None:
            namespaceprefix_ = self.SpecialServices_nsprefix_ + ':' if (UseCapturedNS_ and self.SpecialServices_nsprefix_) else ''
            self.SpecialServices.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SpecialServices', pretty_print=pretty_print)
        if self.Content is not None:
            namespaceprefix_ = self.Content_nsprefix_ + ':' if (UseCapturedNS_ and self.Content_nsprefix_) else ''
            self.Content.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Content', pretty_print=pretty_print)
        if self.GroundOnly is not None:
            namespaceprefix_ = self.GroundOnly_nsprefix_ + ':' if (UseCapturedNS_ and self.GroundOnly_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sGroundOnly>%s</%sGroundOnly>%s' % (namespaceprefix_ , self.gds_format_boolean(self.GroundOnly, input_name='GroundOnly'), namespaceprefix_ , eol_))
        if self.SortBy is not None:
            namespaceprefix_ = self.SortBy_nsprefix_ + ':' if (UseCapturedNS_ and self.SortBy_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSortBy>%s</%sSortBy>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SortBy), input_name='SortBy')), namespaceprefix_ , eol_))
        if self.Machinable is not None:
            namespaceprefix_ = self.Machinable_nsprefix_ + ':' if (UseCapturedNS_ and self.Machinable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMachinable>%s</%sMachinable>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Machinable, input_name='Machinable'), namespaceprefix_ , eol_))
        if self.ReturnLocations is not None:
            namespaceprefix_ = self.ReturnLocations_nsprefix_ + ':' if (UseCapturedNS_ and self.ReturnLocations_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sReturnLocations>%s</%sReturnLocations>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ReturnLocations, input_name='ReturnLocations'), namespaceprefix_ , eol_))
        if self.ReturnServiceInfo is not None:
            namespaceprefix_ = self.ReturnServiceInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.ReturnServiceInfo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sReturnServiceInfo>%s</%sReturnServiceInfo>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ReturnServiceInfo, input_name='ReturnServiceInfo'), namespaceprefix_ , eol_))
        if self.DropOffTime is not None:
            namespaceprefix_ = self.DropOffTime_nsprefix_ + ':' if (UseCapturedNS_ and self.DropOffTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDropOffTime>%s</%sDropOffTime>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DropOffTime), input_name='DropOffTime')), namespaceprefix_ , eol_))
        if self.ShipDate is not None:
            namespaceprefix_ = self.ShipDate_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipDate_nsprefix_) else ''
            self.ShipDate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipDate', pretty_print=pretty_print)
        if self.ReturnDimensionalWeight is not None:
            namespaceprefix_ = self.ReturnDimensionalWeight_nsprefix_ + ':' if (UseCapturedNS_ and self.ReturnDimensionalWeight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sReturnDimensionalWeight>%s</%sReturnDimensionalWeight>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ReturnDimensionalWeight), input_name='ReturnDimensionalWeight')), namespaceprefix_ , eol_))
        if self.TrackingRetentionPeriod is not None:
            namespaceprefix_ = self.TrackingRetentionPeriod_nsprefix_ + ':' if (UseCapturedNS_ and self.TrackingRetentionPeriod_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTrackingRetentionPeriod>%s</%sTrackingRetentionPeriod>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TrackingRetentionPeriod), input_name='TrackingRetentionPeriod')), namespaceprefix_ , eol_))
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
        value = find_attr_value_('ID', node)
        if value is not None and 'ID' not in already_processed:
            already_processed.add('ID')
            self.ID = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Service':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Service')
            value_ = self.gds_validate_string(value_, node, 'Service')
            self.Service = value_
            self.Service_nsprefix_ = child_.prefix
        elif nodeName_ == 'FirstClassMailType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'FirstClassMailType')
            value_ = self.gds_validate_string(value_, node, 'FirstClassMailType')
            self.FirstClassMailType = value_
            self.FirstClassMailType_nsprefix_ = child_.prefix
        elif nodeName_ == 'ZipOrigination':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ZipOrigination')
            value_ = self.gds_validate_string(value_, node, 'ZipOrigination')
            self.ZipOrigination = value_
            self.ZipOrigination_nsprefix_ = child_.prefix
        elif nodeName_ == 'ZipDestination':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ZipDestination')
            value_ = self.gds_validate_string(value_, node, 'ZipDestination')
            self.ZipDestination = value_
            self.ZipDestination_nsprefix_ = child_.prefix
        elif nodeName_ == 'Pounds' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Pounds')
            ival_ = self.gds_validate_integer(ival_, node, 'Pounds')
            self.Pounds = ival_
            self.Pounds_nsprefix_ = child_.prefix
            # validate type PoundsType
            self.validate_PoundsType(self.Pounds)
        elif nodeName_ == 'Ounces' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Ounces')
            fval_ = self.gds_validate_decimal(fval_, node, 'Ounces')
            self.Ounces = fval_
            self.Ounces_nsprefix_ = child_.prefix
            # validate type OuncesType
            self.validate_OuncesType(self.Ounces)
        elif nodeName_ == 'Container':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Container')
            value_ = self.gds_validate_string(value_, node, 'Container')
            self.Container = value_
            self.Container_nsprefix_ = child_.prefix
        elif nodeName_ == 'Size':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Size')
            value_ = self.gds_validate_string(value_, node, 'Size')
            self.Size = value_
            self.Size_nsprefix_ = child_.prefix
        elif nodeName_ == 'Width' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Width')
            fval_ = self.gds_validate_decimal(fval_, node, 'Width')
            self.Width = fval_
            self.Width_nsprefix_ = child_.prefix
        elif nodeName_ == 'Length' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Length')
            fval_ = self.gds_validate_decimal(fval_, node, 'Length')
            self.Length = fval_
            self.Length_nsprefix_ = child_.prefix
        elif nodeName_ == 'Height' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Height')
            fval_ = self.gds_validate_decimal(fval_, node, 'Height')
            self.Height = fval_
            self.Height_nsprefix_ = child_.prefix
        elif nodeName_ == 'Girth' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Girth')
            fval_ = self.gds_validate_decimal(fval_, node, 'Girth')
            self.Girth = fval_
            self.Girth_nsprefix_ = child_.prefix
        elif nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
        elif nodeName_ == 'AmountToCollect':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AmountToCollect')
            value_ = self.gds_validate_string(value_, node, 'AmountToCollect')
            self.AmountToCollect = value_
            self.AmountToCollect_nsprefix_ = child_.prefix
        elif nodeName_ == 'SpecialServices':
            obj_ = SpecialServicesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SpecialServices = obj_
            obj_.original_tagname_ = 'SpecialServices'
        elif nodeName_ == 'Content':
            obj_ = ContentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Content = obj_
            obj_.original_tagname_ = 'Content'
        elif nodeName_ == 'GroundOnly':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'GroundOnly')
            ival_ = self.gds_validate_boolean(ival_, node, 'GroundOnly')
            self.GroundOnly = ival_
            self.GroundOnly_nsprefix_ = child_.prefix
        elif nodeName_ == 'SortBy':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SortBy')
            value_ = self.gds_validate_string(value_, node, 'SortBy')
            self.SortBy = value_
            self.SortBy_nsprefix_ = child_.prefix
        elif nodeName_ == 'Machinable':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Machinable')
            ival_ = self.gds_validate_boolean(ival_, node, 'Machinable')
            self.Machinable = ival_
            self.Machinable_nsprefix_ = child_.prefix
        elif nodeName_ == 'ReturnLocations':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ReturnLocations')
            ival_ = self.gds_validate_boolean(ival_, node, 'ReturnLocations')
            self.ReturnLocations = ival_
            self.ReturnLocations_nsprefix_ = child_.prefix
        elif nodeName_ == 'ReturnServiceInfo':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ReturnServiceInfo')
            ival_ = self.gds_validate_boolean(ival_, node, 'ReturnServiceInfo')
            self.ReturnServiceInfo = ival_
            self.ReturnServiceInfo_nsprefix_ = child_.prefix
        elif nodeName_ == 'DropOffTime':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DropOffTime')
            value_ = self.gds_validate_string(value_, node, 'DropOffTime')
            self.DropOffTime = value_
            self.DropOffTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'ShipDate':
            obj_ = ShipDateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipDate = obj_
            obj_.original_tagname_ = 'ShipDate'
        elif nodeName_ == 'ReturnDimensionalWeight':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ReturnDimensionalWeight')
            value_ = self.gds_validate_string(value_, node, 'ReturnDimensionalWeight')
            self.ReturnDimensionalWeight = value_
            self.ReturnDimensionalWeight_nsprefix_ = child_.prefix
        elif nodeName_ == 'TrackingRetentionPeriod':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TrackingRetentionPeriod')
            value_ = self.gds_validate_string(value_, node, 'TrackingRetentionPeriod')
            self.TrackingRetentionPeriod = value_
            self.TrackingRetentionPeriod_nsprefix_ = child_.prefix
# end class PackageType


class SpecialServicesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SpecialService=None, gds_collector_=None, **kwargs_):
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
    def hasContent_(self):
        if (
            self.SpecialService
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
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SpecialService_ in self.SpecialService:
            namespaceprefix_ = self.SpecialService_nsprefix_ + ':' if (UseCapturedNS_ and self.SpecialService_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSpecialService>%s</%sSpecialService>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(SpecialService_), input_name='SpecialService')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'SpecialService':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SpecialService')
            value_ = self.gds_validate_string(value_, node, 'SpecialService')
            self.SpecialService.append(value_)
            self.SpecialService_nsprefix_ = child_.prefix
# end class SpecialServicesType


class ContentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ContentType_member=None, ContentDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ContentType = ContentType_member
        self.ContentType_nsprefix_ = None
        self.ContentDescription = ContentDescription
        self.ContentDescription_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ContentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ContentType.subclass:
            return ContentType.subclass(*args_, **kwargs_)
        else:
            return ContentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ContentType(self):
        return self.ContentType
    def set_ContentType(self, ContentType):
        self.ContentType = ContentType
    def get_ContentDescription(self):
        return self.ContentDescription
    def set_ContentDescription(self, ContentDescription):
        self.ContentDescription = ContentDescription
    def hasContent_(self):
        if (
            self.ContentType is not None or
            self.ContentDescription is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ContentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ContentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ContentType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ContentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ContentType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ContentType is not None:
            namespaceprefix_ = self.ContentType_nsprefix_ + ':' if (UseCapturedNS_ and self.ContentType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sContentType>%s</%sContentType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ContentType), input_name='ContentType')), namespaceprefix_ , eol_))
        if self.ContentDescription is not None:
            namespaceprefix_ = self.ContentDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.ContentDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sContentDescription>%s</%sContentDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ContentDescription), input_name='ContentDescription')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'ContentType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ContentType')
            value_ = self.gds_validate_string(value_, node, 'ContentType')
            self.ContentType = value_
            self.ContentType_nsprefix_ = child_.prefix
        elif nodeName_ == 'ContentDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ContentDescription')
            value_ = self.gds_validate_string(value_, node, 'ContentDescription')
            self.ContentDescription = value_
            self.ContentDescription_nsprefix_ = child_.prefix
# end class ContentType


class ShipDateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Option=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Option = _cast(None, Option)
        self.Option_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipDateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipDateType.subclass:
            return ShipDateType.subclass(*args_, **kwargs_)
        else:
            return ShipDateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Option(self):
        return self.Option
    def set_Option(self, Option):
        self.Option = Option
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipDateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipDateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipDateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipDateType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipDateType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipDateType'):
        if self.Option is not None and 'Option' not in already_processed:
            already_processed.add('Option')
            outfile.write(' Option=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Option), input_name='Option')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipDateType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Option', node)
        if value is not None and 'Option' not in already_processed:
            already_processed.add('Option')
            self.Option = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ShipDateType


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
        rootTag = 'RateV4Request'
        rootClass = RateV4Request
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
        rootTag = 'RateV4Request'
        rootClass = RateV4Request
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
        rootTag = 'RateV4Request'
        rootClass = RateV4Request
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
        rootTag = 'RateV4Request'
        rootClass = RateV4Request
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from rate_v4_request import *\n\n')
        sys.stdout.write('import rate_v4_request as model_\n\n')
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
    "ContentType",
    "PackageType",
    "RateV4Request",
    "ShipDateType",
    "SpecialServicesType"
]
