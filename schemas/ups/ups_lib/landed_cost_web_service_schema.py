#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Nov 10 10:01:01 2021 by generateDS.py version 2.40.5.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './ups_lib/landed_cost_web_service_schema.py')
#
# Command line arguments:
#   ./schemas/LandedCostWebServiceSchema.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio/.venv/karrio/bin/generateDS --no-namespace-defs -o "./ups_lib/landed_cost_web_service_schema.py" ./schemas/LandedCostWebServiceSchema.xsd
#
# Current working directory (os.getcwd()):
#   ups
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
from lxml import etree as etree_


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
# "xsi:type" attribute value.  See the _exportAttributes method of
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
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
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
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': None,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    setattr(settings[n], self[n])
            from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
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
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
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
            return ('%.15f' % float(input_data)).rstrip('0')
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
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
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
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
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


class LandedCostRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Request=None, QueryRequest=None, EstimateRequest=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Request = Request
        self.Request_nsprefix_ = "lc"
        self.QueryRequest = QueryRequest
        self.QueryRequest_nsprefix_ = "lc"
        self.EstimateRequest = EstimateRequest
        self.EstimateRequest_nsprefix_ = "lc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LandedCostRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LandedCostRequest.subclass:
            return LandedCostRequest.subclass(*args_, **kwargs_)
        else:
            return LandedCostRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Request(self):
        return self.Request
    def set_Request(self, Request):
        self.Request = Request
    def get_QueryRequest(self):
        return self.QueryRequest
    def set_QueryRequest(self, QueryRequest):
        self.QueryRequest = QueryRequest
    def get_EstimateRequest(self):
        return self.EstimateRequest
    def set_EstimateRequest(self, EstimateRequest):
        self.EstimateRequest = EstimateRequest
    def _hasContent(self):
        if (
            self.Request is not None or
            self.QueryRequest is not None or
            self.EstimateRequest is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LandedCostRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LandedCostRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LandedCostRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LandedCostRequest')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LandedCostRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LandedCostRequest'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LandedCostRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Request is not None:
            namespaceprefix_ = self.Request_nsprefix_ + ':' if (UseCapturedNS_ and self.Request_nsprefix_) else ''
            self.Request.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Request', pretty_print=pretty_print)
        if self.QueryRequest is not None:
            namespaceprefix_ = self.QueryRequest_nsprefix_ + ':' if (UseCapturedNS_ and self.QueryRequest_nsprefix_) else ''
            self.QueryRequest.export(outfile, level, namespaceprefix_, namespacedef_='', name_='QueryRequest', pretty_print=pretty_print)
        if self.EstimateRequest is not None:
            namespaceprefix_ = self.EstimateRequest_nsprefix_ + ':' if (UseCapturedNS_ and self.EstimateRequest_nsprefix_) else ''
            self.EstimateRequest.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EstimateRequest', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Request':
            obj_ = RequestTransportType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Request = obj_
            obj_.original_tagname_ = 'Request'
        elif nodeName_ == 'QueryRequest':
            obj_ = QueryRequestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.QueryRequest = obj_
            obj_.original_tagname_ = 'QueryRequest'
        elif nodeName_ == 'EstimateRequest':
            obj_ = EstimateRequestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EstimateRequest = obj_
            obj_.original_tagname_ = 'EstimateRequest'
# end class LandedCostRequest


class LandedCostResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Response=None, QueryResponse=None, EstimateResponse=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Response = Response
        self.Response_nsprefix_ = "lc"
        self.QueryResponse = QueryResponse
        self.QueryResponse_nsprefix_ = "lc"
        self.EstimateResponse = EstimateResponse
        self.EstimateResponse_nsprefix_ = "lc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LandedCostResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LandedCostResponse.subclass:
            return LandedCostResponse.subclass(*args_, **kwargs_)
        else:
            return LandedCostResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def get_QueryResponse(self):
        return self.QueryResponse
    def set_QueryResponse(self, QueryResponse):
        self.QueryResponse = QueryResponse
    def get_EstimateResponse(self):
        return self.EstimateResponse
    def set_EstimateResponse(self, EstimateResponse):
        self.EstimateResponse = EstimateResponse
    def _hasContent(self):
        if (
            self.Response is not None or
            self.QueryResponse is not None or
            self.EstimateResponse is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LandedCostResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LandedCostResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LandedCostResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LandedCostResponse')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LandedCostResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LandedCostResponse'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LandedCostResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Response is not None:
            namespaceprefix_ = self.Response_nsprefix_ + ':' if (UseCapturedNS_ and self.Response_nsprefix_) else ''
            self.Response.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Response', pretty_print=pretty_print)
        if self.QueryResponse is not None:
            namespaceprefix_ = self.QueryResponse_nsprefix_ + ':' if (UseCapturedNS_ and self.QueryResponse_nsprefix_) else ''
            self.QueryResponse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='QueryResponse', pretty_print=pretty_print)
        if self.EstimateResponse is not None:
            namespaceprefix_ = self.EstimateResponse_nsprefix_ + ':' if (UseCapturedNS_ and self.EstimateResponse_nsprefix_) else ''
            self.EstimateResponse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EstimateResponse', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Response':
            obj_ = ResponseTransportType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Response = obj_
            obj_.original_tagname_ = 'Response'
        elif nodeName_ == 'QueryResponse':
            obj_ = QueryResponseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.QueryResponse = obj_
            obj_.original_tagname_ = 'QueryResponse'
        elif nodeName_ == 'EstimateResponse':
            obj_ = EstimateResponseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EstimateResponse = obj_
            obj_.original_tagname_ = 'EstimateResponse'
# end class LandedCostResponse


class RequestTransportType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RequestAction=None, RequestOption=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.RequestAction = RequestAction
        self.RequestAction_nsprefix_ = None
        if RequestOption is None:
            self.RequestOption = []
        else:
            self.RequestOption = RequestOption
        self.RequestOption_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RequestTransportType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RequestTransportType.subclass:
            return RequestTransportType.subclass(*args_, **kwargs_)
        else:
            return RequestTransportType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RequestAction(self):
        return self.RequestAction
    def set_RequestAction(self, RequestAction):
        self.RequestAction = RequestAction
    def get_RequestOption(self):
        return self.RequestOption
    def set_RequestOption(self, RequestOption):
        self.RequestOption = RequestOption
    def add_RequestOption(self, value):
        self.RequestOption.append(value)
    def insert_RequestOption_at(self, index, value):
        self.RequestOption.insert(index, value)
    def replace_RequestOption_at(self, index, value):
        self.RequestOption[index] = value
    def _hasContent(self):
        if (
            self.RequestAction is not None or
            self.RequestOption
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestTransportType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RequestTransportType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RequestTransportType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RequestTransportType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RequestTransportType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RequestTransportType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestTransportType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.RequestAction is not None:
            namespaceprefix_ = self.RequestAction_nsprefix_ + ':' if (UseCapturedNS_ and self.RequestAction_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRequestAction>%s</%sRequestAction>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RequestAction), input_name='RequestAction')), namespaceprefix_ , eol_))
        for RequestOption_ in self.RequestOption:
            namespaceprefix_ = self.RequestOption_nsprefix_ + ':' if (UseCapturedNS_ and self.RequestOption_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRequestOption>%s</%sRequestOption>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(RequestOption_), input_name='RequestOption')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RequestAction':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RequestAction')
            value_ = self.gds_validate_string(value_, node, 'RequestAction')
            self.RequestAction = value_
            self.RequestAction_nsprefix_ = child_.prefix
        elif nodeName_ == 'RequestOption':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RequestOption')
            value_ = self.gds_validate_string(value_, node, 'RequestOption')
            self.RequestOption.append(value_)
            self.RequestOption_nsprefix_ = child_.prefix
# end class RequestTransportType


class QueryRequestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Shipment=None, TransactionReferenceID=None, SuppressQuestionIndicator=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Shipment = Shipment
        self.Shipment_nsprefix_ = "lc"
        if TransactionReferenceID is None:
            self.TransactionReferenceID = []
        else:
            self.TransactionReferenceID = TransactionReferenceID
        self.TransactionReferenceID_nsprefix_ = None
        self.SuppressQuestionIndicator = SuppressQuestionIndicator
        self.SuppressQuestionIndicator_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryRequestType.subclass:
            return QueryRequestType.subclass(*args_, **kwargs_)
        else:
            return QueryRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Shipment(self):
        return self.Shipment
    def set_Shipment(self, Shipment):
        self.Shipment = Shipment
    def get_TransactionReferenceID(self):
        return self.TransactionReferenceID
    def set_TransactionReferenceID(self, TransactionReferenceID):
        self.TransactionReferenceID = TransactionReferenceID
    def add_TransactionReferenceID(self, value):
        self.TransactionReferenceID.append(value)
    def insert_TransactionReferenceID_at(self, index, value):
        self.TransactionReferenceID.insert(index, value)
    def replace_TransactionReferenceID_at(self, index, value):
        self.TransactionReferenceID[index] = value
    def get_SuppressQuestionIndicator(self):
        return self.SuppressQuestionIndicator
    def set_SuppressQuestionIndicator(self, SuppressQuestionIndicator):
        self.SuppressQuestionIndicator = SuppressQuestionIndicator
    def _hasContent(self):
        if (
            self.Shipment is not None or
            self.TransactionReferenceID or
            self.SuppressQuestionIndicator is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='QueryRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryRequestType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='QueryRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Shipment is not None:
            namespaceprefix_ = self.Shipment_nsprefix_ + ':' if (UseCapturedNS_ and self.Shipment_nsprefix_) else ''
            self.Shipment.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Shipment', pretty_print=pretty_print)
        for TransactionReferenceID_ in self.TransactionReferenceID:
            namespaceprefix_ = self.TransactionReferenceID_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionReferenceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransactionReferenceID>%s</%sTransactionReferenceID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(TransactionReferenceID_), input_name='TransactionReferenceID')), namespaceprefix_ , eol_))
        if self.SuppressQuestionIndicator is not None:
            namespaceprefix_ = self.SuppressQuestionIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.SuppressQuestionIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSuppressQuestionIndicator>%s</%sSuppressQuestionIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SuppressQuestionIndicator), input_name='SuppressQuestionIndicator')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Shipment':
            obj_ = ShipmentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Shipment = obj_
            obj_.original_tagname_ = 'Shipment'
        elif nodeName_ == 'TransactionReferenceID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransactionReferenceID')
            value_ = self.gds_validate_string(value_, node, 'TransactionReferenceID')
            self.TransactionReferenceID.append(value_)
            self.TransactionReferenceID_nsprefix_ = child_.prefix
        elif nodeName_ == 'SuppressQuestionIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SuppressQuestionIndicator')
            value_ = self.gds_validate_string(value_, node, 'SuppressQuestionIndicator')
            self.SuppressQuestionIndicator = value_
            self.SuppressQuestionIndicator_nsprefix_ = child_.prefix
# end class QueryRequestType


class EstimateRequestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Shipment=None, TransactionDigest=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Shipment = Shipment
        self.Shipment_nsprefix_ = "lc"
        self.TransactionDigest = TransactionDigest
        self.TransactionDigest_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EstimateRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EstimateRequestType.subclass:
            return EstimateRequestType.subclass(*args_, **kwargs_)
        else:
            return EstimateRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Shipment(self):
        return self.Shipment
    def set_Shipment(self, Shipment):
        self.Shipment = Shipment
    def get_TransactionDigest(self):
        return self.TransactionDigest
    def set_TransactionDigest(self, TransactionDigest):
        self.TransactionDigest = TransactionDigest
    def _hasContent(self):
        if (
            self.Shipment is not None or
            self.TransactionDigest is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EstimateRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EstimateRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EstimateRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EstimateRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EstimateRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EstimateRequestType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EstimateRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Shipment is not None:
            namespaceprefix_ = self.Shipment_nsprefix_ + ':' if (UseCapturedNS_ and self.Shipment_nsprefix_) else ''
            self.Shipment.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Shipment', pretty_print=pretty_print)
        if self.TransactionDigest is not None:
            namespaceprefix_ = self.TransactionDigest_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionDigest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransactionDigest>%s</%sTransactionDigest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TransactionDigest), input_name='TransactionDigest')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Shipment':
            obj_ = ShipmentAnswerType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Shipment = obj_
            obj_.original_tagname_ = 'Shipment'
        elif nodeName_ == 'TransactionDigest':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransactionDigest')
            value_ = self.gds_validate_string(value_, node, 'TransactionDigest')
            self.TransactionDigest = value_
            self.TransactionDigest_nsprefix_ = child_.prefix
# end class EstimateRequestType


class ResponseTransportType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Warning=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Warning is None:
            self.Warning = []
        else:
            self.Warning = Warning
        self.Warning_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResponseTransportType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResponseTransportType.subclass:
            return ResponseTransportType.subclass(*args_, **kwargs_)
        else:
            return ResponseTransportType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Warning(self):
        return self.Warning
    def set_Warning(self, Warning):
        self.Warning = Warning
    def add_Warning(self, value):
        self.Warning.append(value)
    def insert_Warning_at(self, index, value):
        self.Warning.insert(index, value)
    def replace_Warning_at(self, index, value):
        self.Warning[index] = value
    def _hasContent(self):
        if (
            self.Warning
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseTransportType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResponseTransportType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResponseTransportType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseTransportType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResponseTransportType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ResponseTransportType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseTransportType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Warning_ in self.Warning:
            namespaceprefix_ = self.Warning_nsprefix_ + ':' if (UseCapturedNS_ and self.Warning_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sWarning>%s</%sWarning>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Warning_), input_name='Warning')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Warning':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Warning')
            value_ = self.gds_validate_string(value_, node, 'Warning')
            self.Warning.append(value_)
            self.Warning_nsprefix_ = child_.prefix
# end class ResponseTransportType


class QueryResponseType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Shipment=None, TransactionDigest=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Shipment = Shipment
        self.Shipment_nsprefix_ = "lc"
        self.TransactionDigest = TransactionDigest
        self.TransactionDigest_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryResponseType.subclass:
            return QueryResponseType.subclass(*args_, **kwargs_)
        else:
            return QueryResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Shipment(self):
        return self.Shipment
    def set_Shipment(self, Shipment):
        self.Shipment = Shipment
    def get_TransactionDigest(self):
        return self.TransactionDigest
    def set_TransactionDigest(self, TransactionDigest):
        self.TransactionDigest = TransactionDigest
    def _hasContent(self):
        if (
            self.Shipment is not None or
            self.TransactionDigest is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='QueryResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryResponseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='QueryResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Shipment is not None:
            namespaceprefix_ = self.Shipment_nsprefix_ + ':' if (UseCapturedNS_ and self.Shipment_nsprefix_) else ''
            self.Shipment.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Shipment', pretty_print=pretty_print)
        if self.TransactionDigest is not None:
            namespaceprefix_ = self.TransactionDigest_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionDigest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransactionDigest>%s</%sTransactionDigest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TransactionDigest), input_name='TransactionDigest')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Shipment':
            obj_ = ShipmentResultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Shipment = obj_
            obj_.original_tagname_ = 'Shipment'
        elif nodeName_ == 'TransactionDigest':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransactionDigest')
            value_ = self.gds_validate_string(value_, node, 'TransactionDigest')
            self.TransactionDigest = value_
            self.TransactionDigest_nsprefix_ = child_.prefix
# end class QueryResponseType


class EstimateResponseType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TransactionInfo=None, ShipmentEstimate=None, SuppressQuestionIndicator=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TransactionInfo = TransactionInfo
        self.TransactionInfo_nsprefix_ = "lc"
        self.ShipmentEstimate = ShipmentEstimate
        self.ShipmentEstimate_nsprefix_ = "lc"
        self.SuppressQuestionIndicator = SuppressQuestionIndicator
        self.SuppressQuestionIndicator_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EstimateResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EstimateResponseType.subclass:
            return EstimateResponseType.subclass(*args_, **kwargs_)
        else:
            return EstimateResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TransactionInfo(self):
        return self.TransactionInfo
    def set_TransactionInfo(self, TransactionInfo):
        self.TransactionInfo = TransactionInfo
    def get_ShipmentEstimate(self):
        return self.ShipmentEstimate
    def set_ShipmentEstimate(self, ShipmentEstimate):
        self.ShipmentEstimate = ShipmentEstimate
    def get_SuppressQuestionIndicator(self):
        return self.SuppressQuestionIndicator
    def set_SuppressQuestionIndicator(self, SuppressQuestionIndicator):
        self.SuppressQuestionIndicator = SuppressQuestionIndicator
    def _hasContent(self):
        if (
            self.TransactionInfo is not None or
            self.ShipmentEstimate is not None or
            self.SuppressQuestionIndicator is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EstimateResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EstimateResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EstimateResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EstimateResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EstimateResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EstimateResponseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EstimateResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TransactionInfo is not None:
            namespaceprefix_ = self.TransactionInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionInfo_nsprefix_) else ''
            self.TransactionInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TransactionInfo', pretty_print=pretty_print)
        if self.ShipmentEstimate is not None:
            namespaceprefix_ = self.ShipmentEstimate_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipmentEstimate_nsprefix_) else ''
            self.ShipmentEstimate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipmentEstimate', pretty_print=pretty_print)
        if self.SuppressQuestionIndicator is not None:
            namespaceprefix_ = self.SuppressQuestionIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.SuppressQuestionIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSuppressQuestionIndicator>%s</%sSuppressQuestionIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SuppressQuestionIndicator), input_name='SuppressQuestionIndicator')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TransactionInfo':
            obj_ = TransactionInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TransactionInfo = obj_
            obj_.original_tagname_ = 'TransactionInfo'
        elif nodeName_ == 'ShipmentEstimate':
            obj_ = ShipmentEstimateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipmentEstimate = obj_
            obj_.original_tagname_ = 'ShipmentEstimate'
        elif nodeName_ == 'SuppressQuestionIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SuppressQuestionIndicator')
            value_ = self.gds_validate_string(value_, node, 'SuppressQuestionIndicator')
            self.SuppressQuestionIndicator = value_
            self.SuppressQuestionIndicator_nsprefix_ = child_.prefix
# end class EstimateResponseType


class ShipmentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, OriginCountryCode=None, OriginStateProvinceCode=None, DestinationCountryCode=None, DestinationStateProvinceCode=None, TransportationMode=None, FreightCharges=None, AdditionalInsurance=None, Product=None, ResultCurrencyCode=None, TariffCodeAlert=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.OriginCountryCode = OriginCountryCode
        self.OriginCountryCode_nsprefix_ = None
        self.OriginStateProvinceCode = OriginStateProvinceCode
        self.OriginStateProvinceCode_nsprefix_ = None
        self.DestinationCountryCode = DestinationCountryCode
        self.DestinationCountryCode_nsprefix_ = None
        self.DestinationStateProvinceCode = DestinationStateProvinceCode
        self.DestinationStateProvinceCode_nsprefix_ = None
        self.TransportationMode = TransportationMode
        self.TransportationMode_nsprefix_ = None
        self.FreightCharges = FreightCharges
        self.FreightCharges_nsprefix_ = "lc"
        self.AdditionalInsurance = AdditionalInsurance
        self.AdditionalInsurance_nsprefix_ = "lc"
        if Product is None:
            self.Product = []
        else:
            self.Product = Product
        self.Product_nsprefix_ = "lc"
        self.ResultCurrencyCode = ResultCurrencyCode
        self.ResultCurrencyCode_nsprefix_ = None
        self.TariffCodeAlert = TariffCodeAlert
        self.TariffCodeAlert_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentType.subclass:
            return ShipmentType.subclass(*args_, **kwargs_)
        else:
            return ShipmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_OriginCountryCode(self):
        return self.OriginCountryCode
    def set_OriginCountryCode(self, OriginCountryCode):
        self.OriginCountryCode = OriginCountryCode
    def get_OriginStateProvinceCode(self):
        return self.OriginStateProvinceCode
    def set_OriginStateProvinceCode(self, OriginStateProvinceCode):
        self.OriginStateProvinceCode = OriginStateProvinceCode
    def get_DestinationCountryCode(self):
        return self.DestinationCountryCode
    def set_DestinationCountryCode(self, DestinationCountryCode):
        self.DestinationCountryCode = DestinationCountryCode
    def get_DestinationStateProvinceCode(self):
        return self.DestinationStateProvinceCode
    def set_DestinationStateProvinceCode(self, DestinationStateProvinceCode):
        self.DestinationStateProvinceCode = DestinationStateProvinceCode
    def get_TransportationMode(self):
        return self.TransportationMode
    def set_TransportationMode(self, TransportationMode):
        self.TransportationMode = TransportationMode
    def get_FreightCharges(self):
        return self.FreightCharges
    def set_FreightCharges(self, FreightCharges):
        self.FreightCharges = FreightCharges
    def get_AdditionalInsurance(self):
        return self.AdditionalInsurance
    def set_AdditionalInsurance(self, AdditionalInsurance):
        self.AdditionalInsurance = AdditionalInsurance
    def get_Product(self):
        return self.Product
    def set_Product(self, Product):
        self.Product = Product
    def add_Product(self, value):
        self.Product.append(value)
    def insert_Product_at(self, index, value):
        self.Product.insert(index, value)
    def replace_Product_at(self, index, value):
        self.Product[index] = value
    def get_ResultCurrencyCode(self):
        return self.ResultCurrencyCode
    def set_ResultCurrencyCode(self, ResultCurrencyCode):
        self.ResultCurrencyCode = ResultCurrencyCode
    def get_TariffCodeAlert(self):
        return self.TariffCodeAlert
    def set_TariffCodeAlert(self, TariffCodeAlert):
        self.TariffCodeAlert = TariffCodeAlert
    def _hasContent(self):
        if (
            self.OriginCountryCode is not None or
            self.OriginStateProvinceCode is not None or
            self.DestinationCountryCode is not None or
            self.DestinationStateProvinceCode is not None or
            self.TransportationMode is not None or
            self.FreightCharges is not None or
            self.AdditionalInsurance is not None or
            self.Product or
            self.ResultCurrencyCode is not None or
            self.TariffCodeAlert is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.OriginCountryCode is not None:
            namespaceprefix_ = self.OriginCountryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.OriginCountryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOriginCountryCode>%s</%sOriginCountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OriginCountryCode), input_name='OriginCountryCode')), namespaceprefix_ , eol_))
        if self.OriginStateProvinceCode is not None:
            namespaceprefix_ = self.OriginStateProvinceCode_nsprefix_ + ':' if (UseCapturedNS_ and self.OriginStateProvinceCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOriginStateProvinceCode>%s</%sOriginStateProvinceCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OriginStateProvinceCode), input_name='OriginStateProvinceCode')), namespaceprefix_ , eol_))
        if self.DestinationCountryCode is not None:
            namespaceprefix_ = self.DestinationCountryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.DestinationCountryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDestinationCountryCode>%s</%sDestinationCountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DestinationCountryCode), input_name='DestinationCountryCode')), namespaceprefix_ , eol_))
        if self.DestinationStateProvinceCode is not None:
            namespaceprefix_ = self.DestinationStateProvinceCode_nsprefix_ + ':' if (UseCapturedNS_ and self.DestinationStateProvinceCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDestinationStateProvinceCode>%s</%sDestinationStateProvinceCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DestinationStateProvinceCode), input_name='DestinationStateProvinceCode')), namespaceprefix_ , eol_))
        if self.TransportationMode is not None:
            namespaceprefix_ = self.TransportationMode_nsprefix_ + ':' if (UseCapturedNS_ and self.TransportationMode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransportationMode>%s</%sTransportationMode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TransportationMode), input_name='TransportationMode')), namespaceprefix_ , eol_))
        if self.FreightCharges is not None:
            namespaceprefix_ = self.FreightCharges_nsprefix_ + ':' if (UseCapturedNS_ and self.FreightCharges_nsprefix_) else ''
            self.FreightCharges.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FreightCharges', pretty_print=pretty_print)
        if self.AdditionalInsurance is not None:
            namespaceprefix_ = self.AdditionalInsurance_nsprefix_ + ':' if (UseCapturedNS_ and self.AdditionalInsurance_nsprefix_) else ''
            self.AdditionalInsurance.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AdditionalInsurance', pretty_print=pretty_print)
        for Product_ in self.Product:
            namespaceprefix_ = self.Product_nsprefix_ + ':' if (UseCapturedNS_ and self.Product_nsprefix_) else ''
            Product_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Product', pretty_print=pretty_print)
        if self.ResultCurrencyCode is not None:
            namespaceprefix_ = self.ResultCurrencyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResultCurrencyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResultCurrencyCode>%s</%sResultCurrencyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResultCurrencyCode), input_name='ResultCurrencyCode')), namespaceprefix_ , eol_))
        if self.TariffCodeAlert is not None:
            namespaceprefix_ = self.TariffCodeAlert_nsprefix_ + ':' if (UseCapturedNS_ and self.TariffCodeAlert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTariffCodeAlert>%s</%sTariffCodeAlert>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TariffCodeAlert), input_name='TariffCodeAlert')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OriginCountryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OriginCountryCode')
            value_ = self.gds_validate_string(value_, node, 'OriginCountryCode')
            self.OriginCountryCode = value_
            self.OriginCountryCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'OriginStateProvinceCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OriginStateProvinceCode')
            value_ = self.gds_validate_string(value_, node, 'OriginStateProvinceCode')
            self.OriginStateProvinceCode = value_
            self.OriginStateProvinceCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'DestinationCountryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DestinationCountryCode')
            value_ = self.gds_validate_string(value_, node, 'DestinationCountryCode')
            self.DestinationCountryCode = value_
            self.DestinationCountryCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'DestinationStateProvinceCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DestinationStateProvinceCode')
            value_ = self.gds_validate_string(value_, node, 'DestinationStateProvinceCode')
            self.DestinationStateProvinceCode = value_
            self.DestinationStateProvinceCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'TransportationMode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransportationMode')
            value_ = self.gds_validate_string(value_, node, 'TransportationMode')
            self.TransportationMode = value_
            self.TransportationMode_nsprefix_ = child_.prefix
        elif nodeName_ == 'FreightCharges':
            obj_ = ChargesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FreightCharges = obj_
            obj_.original_tagname_ = 'FreightCharges'
        elif nodeName_ == 'AdditionalInsurance':
            obj_ = ChargesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AdditionalInsurance = obj_
            obj_.original_tagname_ = 'AdditionalInsurance'
        elif nodeName_ == 'Product':
            obj_ = ProductType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Product.append(obj_)
            obj_.original_tagname_ = 'Product'
        elif nodeName_ == 'ResultCurrencyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResultCurrencyCode')
            value_ = self.gds_validate_string(value_, node, 'ResultCurrencyCode')
            self.ResultCurrencyCode = value_
            self.ResultCurrencyCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'TariffCodeAlert':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TariffCodeAlert')
            value_ = self.gds_validate_string(value_, node, 'TariffCodeAlert')
            self.TariffCodeAlert = value_
            self.TariffCodeAlert_nsprefix_ = child_.prefix
# end class ShipmentType


class ShipmentResultType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Product=None, Question=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Product is None:
            self.Product = []
        else:
            self.Product = Product
        self.Product_nsprefix_ = "lc"
        if Question is None:
            self.Question = []
        else:
            self.Question = Question
        self.Question_nsprefix_ = "lc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentResultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentResultType.subclass:
            return ShipmentResultType.subclass(*args_, **kwargs_)
        else:
            return ShipmentResultType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Product(self):
        return self.Product
    def set_Product(self, Product):
        self.Product = Product
    def add_Product(self, value):
        self.Product.append(value)
    def insert_Product_at(self, index, value):
        self.Product.insert(index, value)
    def replace_Product_at(self, index, value):
        self.Product[index] = value
    def get_Question(self):
        return self.Question
    def set_Question(self, Question):
        self.Question = Question
    def add_Question(self, value):
        self.Question.append(value)
    def insert_Question_at(self, index, value):
        self.Question.insert(index, value)
    def replace_Question_at(self, index, value):
        self.Question[index] = value
    def _hasContent(self):
        if (
            self.Product or
            self.Question
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentResultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentResultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentResultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentResultType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentResultType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentResultType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentResultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Product_ in self.Product:
            namespaceprefix_ = self.Product_nsprefix_ + ':' if (UseCapturedNS_ and self.Product_nsprefix_) else ''
            Product_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Product', pretty_print=pretty_print)
        for Question_ in self.Question:
            namespaceprefix_ = self.Question_nsprefix_ + ':' if (UseCapturedNS_ and self.Question_nsprefix_) else ''
            Question_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Question', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Product':
            obj_ = ProductResultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Product.append(obj_)
            obj_.original_tagname_ = 'Product'
        elif nodeName_ == 'Question':
            obj_ = QuestionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Question.append(obj_)
            obj_.original_tagname_ = 'Question'
# end class ShipmentResultType


class ShipmentAnswerType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Product=None, Question=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Product is None:
            self.Product = []
        else:
            self.Product = Product
        self.Product_nsprefix_ = "lc"
        if Question is None:
            self.Question = []
        else:
            self.Question = Question
        self.Question_nsprefix_ = "lc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentAnswerType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentAnswerType.subclass:
            return ShipmentAnswerType.subclass(*args_, **kwargs_)
        else:
            return ShipmentAnswerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Product(self):
        return self.Product
    def set_Product(self, Product):
        self.Product = Product
    def add_Product(self, value):
        self.Product.append(value)
    def insert_Product_at(self, index, value):
        self.Product.insert(index, value)
    def replace_Product_at(self, index, value):
        self.Product[index] = value
    def get_Question(self):
        return self.Question
    def set_Question(self, Question):
        self.Question = Question
    def add_Question(self, value):
        self.Question.append(value)
    def insert_Question_at(self, index, value):
        self.Question.insert(index, value)
    def replace_Question_at(self, index, value):
        self.Question[index] = value
    def _hasContent(self):
        if (
            self.Product or
            self.Question
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentAnswerType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentAnswerType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentAnswerType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentAnswerType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentAnswerType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentAnswerType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentAnswerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Product_ in self.Product:
            namespaceprefix_ = self.Product_nsprefix_ + ':' if (UseCapturedNS_ and self.Product_nsprefix_) else ''
            Product_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Product', pretty_print=pretty_print)
        for Question_ in self.Question:
            namespaceprefix_ = self.Question_nsprefix_ + ':' if (UseCapturedNS_ and self.Question_nsprefix_) else ''
            Question_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Question', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Product':
            obj_ = ProductAnswerType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Product.append(obj_)
            obj_.original_tagname_ = 'Product'
        elif nodeName_ == 'Question':
            obj_ = AnswerType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Question.append(obj_)
            obj_.original_tagname_ = 'Question'
# end class ShipmentAnswerType


class ShipmentEstimateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CurrencyCode=None, ShipmentCharges=None, ProductsCharges=None, TotalLandedCost=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CurrencyCode = CurrencyCode
        self.CurrencyCode_nsprefix_ = None
        self.ShipmentCharges = ShipmentCharges
        self.ShipmentCharges_nsprefix_ = "lc"
        self.ProductsCharges = ProductsCharges
        self.ProductsCharges_nsprefix_ = "lc"
        self.TotalLandedCost = TotalLandedCost
        self.TotalLandedCost_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentEstimateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentEstimateType.subclass:
            return ShipmentEstimateType.subclass(*args_, **kwargs_)
        else:
            return ShipmentEstimateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CurrencyCode(self):
        return self.CurrencyCode
    def set_CurrencyCode(self, CurrencyCode):
        self.CurrencyCode = CurrencyCode
    def get_ShipmentCharges(self):
        return self.ShipmentCharges
    def set_ShipmentCharges(self, ShipmentCharges):
        self.ShipmentCharges = ShipmentCharges
    def get_ProductsCharges(self):
        return self.ProductsCharges
    def set_ProductsCharges(self, ProductsCharges):
        self.ProductsCharges = ProductsCharges
    def get_TotalLandedCost(self):
        return self.TotalLandedCost
    def set_TotalLandedCost(self, TotalLandedCost):
        self.TotalLandedCost = TotalLandedCost
    def _hasContent(self):
        if (
            self.CurrencyCode is not None or
            self.ShipmentCharges is not None or
            self.ProductsCharges is not None or
            self.TotalLandedCost is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentEstimateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentEstimateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentEstimateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentEstimateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentEstimateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentEstimateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentEstimateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CurrencyCode is not None:
            namespaceprefix_ = self.CurrencyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CurrencyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCurrencyCode>%s</%sCurrencyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CurrencyCode), input_name='CurrencyCode')), namespaceprefix_ , eol_))
        if self.ShipmentCharges is not None:
            namespaceprefix_ = self.ShipmentCharges_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipmentCharges_nsprefix_) else ''
            self.ShipmentCharges.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipmentCharges', pretty_print=pretty_print)
        if self.ProductsCharges is not None:
            namespaceprefix_ = self.ProductsCharges_nsprefix_ + ':' if (UseCapturedNS_ and self.ProductsCharges_nsprefix_) else ''
            self.ProductsCharges.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ProductsCharges', pretty_print=pretty_print)
        if self.TotalLandedCost is not None:
            namespaceprefix_ = self.TotalLandedCost_nsprefix_ + ':' if (UseCapturedNS_ and self.TotalLandedCost_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTotalLandedCost>%s</%sTotalLandedCost>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TotalLandedCost), input_name='TotalLandedCost')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CurrencyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CurrencyCode')
            value_ = self.gds_validate_string(value_, node, 'CurrencyCode')
            self.CurrencyCode = value_
            self.CurrencyCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'ShipmentCharges':
            obj_ = ShipmentChargesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipmentCharges = obj_
            obj_.original_tagname_ = 'ShipmentCharges'
        elif nodeName_ == 'ProductsCharges':
            obj_ = ProductsChargesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ProductsCharges = obj_
            obj_.original_tagname_ = 'ProductsCharges'
        elif nodeName_ == 'TotalLandedCost':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TotalLandedCost')
            value_ = self.gds_validate_string(value_, node, 'TotalLandedCost')
            self.TotalLandedCost = value_
            self.TotalLandedCost_nsprefix_ = child_.prefix
# end class ShipmentEstimateType


class TransactionInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Date=None, Time=None, TransactionCharge=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Date = Date
        self.Date_nsprefix_ = None
        self.Time = Time
        self.Time_nsprefix_ = None
        self.TransactionCharge = TransactionCharge
        self.TransactionCharge_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransactionInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransactionInfoType.subclass:
            return TransactionInfoType.subclass(*args_, **kwargs_)
        else:
            return TransactionInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Date(self):
        return self.Date
    def set_Date(self, Date):
        self.Date = Date
    def get_Time(self):
        return self.Time
    def set_Time(self, Time):
        self.Time = Time
    def get_TransactionCharge(self):
        return self.TransactionCharge
    def set_TransactionCharge(self, TransactionCharge):
        self.TransactionCharge = TransactionCharge
    def _hasContent(self):
        if (
            self.Date is not None or
            self.Time is not None or
            self.TransactionCharge is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TransactionInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransactionInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransactionInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransactionInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransactionInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TransactionInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TransactionInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Date is not None:
            namespaceprefix_ = self.Date_nsprefix_ + ':' if (UseCapturedNS_ and self.Date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDate>%s</%sDate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Date), input_name='Date')), namespaceprefix_ , eol_))
        if self.Time is not None:
            namespaceprefix_ = self.Time_nsprefix_ + ':' if (UseCapturedNS_ and self.Time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTime>%s</%sTime>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Time), input_name='Time')), namespaceprefix_ , eol_))
        if self.TransactionCharge is not None:
            namespaceprefix_ = self.TransactionCharge_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionCharge_nsprefix_) else ''
            self.TransactionCharge.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TransactionCharge', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Date')
            value_ = self.gds_validate_string(value_, node, 'Date')
            self.Date = value_
            self.Date_nsprefix_ = child_.prefix
        elif nodeName_ == 'Time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Time')
            value_ = self.gds_validate_string(value_, node, 'Time')
            self.Time = value_
            self.Time_nsprefix_ = child_.prefix
        elif nodeName_ == 'TransactionCharge':
            obj_ = TransactionChargeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TransactionCharge = obj_
            obj_.original_tagname_ = 'TransactionCharge'
# end class TransactionInfoType


class ProductType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ProductName=None, ProductDescription=None, ProductCountryCodeOfOrigin=None, TariffInfo=None, Quantity=None, UnitPrice=None, Weight=None, TariffCodeAlert=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ProductName = ProductName
        self.ProductName_nsprefix_ = None
        self.ProductDescription = ProductDescription
        self.ProductDescription_nsprefix_ = None
        self.ProductCountryCodeOfOrigin = ProductCountryCodeOfOrigin
        self.ProductCountryCodeOfOrigin_nsprefix_ = None
        self.TariffInfo = TariffInfo
        self.TariffInfo_nsprefix_ = "lc"
        self.Quantity = Quantity
        self.Quantity_nsprefix_ = "lc"
        self.UnitPrice = UnitPrice
        self.UnitPrice_nsprefix_ = "lc"
        self.Weight = Weight
        self.Weight_nsprefix_ = "lc"
        self.TariffCodeAlert = TariffCodeAlert
        self.TariffCodeAlert_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductType.subclass:
            return ProductType.subclass(*args_, **kwargs_)
        else:
            return ProductType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ProductName(self):
        return self.ProductName
    def set_ProductName(self, ProductName):
        self.ProductName = ProductName
    def get_ProductDescription(self):
        return self.ProductDescription
    def set_ProductDescription(self, ProductDescription):
        self.ProductDescription = ProductDescription
    def get_ProductCountryCodeOfOrigin(self):
        return self.ProductCountryCodeOfOrigin
    def set_ProductCountryCodeOfOrigin(self, ProductCountryCodeOfOrigin):
        self.ProductCountryCodeOfOrigin = ProductCountryCodeOfOrigin
    def get_TariffInfo(self):
        return self.TariffInfo
    def set_TariffInfo(self, TariffInfo):
        self.TariffInfo = TariffInfo
    def get_Quantity(self):
        return self.Quantity
    def set_Quantity(self, Quantity):
        self.Quantity = Quantity
    def get_UnitPrice(self):
        return self.UnitPrice
    def set_UnitPrice(self, UnitPrice):
        self.UnitPrice = UnitPrice
    def get_Weight(self):
        return self.Weight
    def set_Weight(self, Weight):
        self.Weight = Weight
    def get_TariffCodeAlert(self):
        return self.TariffCodeAlert
    def set_TariffCodeAlert(self, TariffCodeAlert):
        self.TariffCodeAlert = TariffCodeAlert
    def _hasContent(self):
        if (
            self.ProductName is not None or
            self.ProductDescription is not None or
            self.ProductCountryCodeOfOrigin is not None or
            self.TariffInfo is not None or
            self.Quantity is not None or
            self.UnitPrice is not None or
            self.Weight is not None or
            self.TariffCodeAlert is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ProductName is not None:
            namespaceprefix_ = self.ProductName_nsprefix_ + ':' if (UseCapturedNS_ and self.ProductName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sProductName>%s</%sProductName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ProductName), input_name='ProductName')), namespaceprefix_ , eol_))
        if self.ProductDescription is not None:
            namespaceprefix_ = self.ProductDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.ProductDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sProductDescription>%s</%sProductDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ProductDescription), input_name='ProductDescription')), namespaceprefix_ , eol_))
        if self.ProductCountryCodeOfOrigin is not None:
            namespaceprefix_ = self.ProductCountryCodeOfOrigin_nsprefix_ + ':' if (UseCapturedNS_ and self.ProductCountryCodeOfOrigin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sProductCountryCodeOfOrigin>%s</%sProductCountryCodeOfOrigin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ProductCountryCodeOfOrigin), input_name='ProductCountryCodeOfOrigin')), namespaceprefix_ , eol_))
        if self.TariffInfo is not None:
            namespaceprefix_ = self.TariffInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.TariffInfo_nsprefix_) else ''
            self.TariffInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TariffInfo', pretty_print=pretty_print)
        if self.Quantity is not None:
            namespaceprefix_ = self.Quantity_nsprefix_ + ':' if (UseCapturedNS_ and self.Quantity_nsprefix_) else ''
            self.Quantity.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Quantity', pretty_print=pretty_print)
        if self.UnitPrice is not None:
            namespaceprefix_ = self.UnitPrice_nsprefix_ + ':' if (UseCapturedNS_ and self.UnitPrice_nsprefix_) else ''
            self.UnitPrice.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnitPrice', pretty_print=pretty_print)
        if self.Weight is not None:
            namespaceprefix_ = self.Weight_nsprefix_ + ':' if (UseCapturedNS_ and self.Weight_nsprefix_) else ''
            self.Weight.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Weight', pretty_print=pretty_print)
        if self.TariffCodeAlert is not None:
            namespaceprefix_ = self.TariffCodeAlert_nsprefix_ + ':' if (UseCapturedNS_ and self.TariffCodeAlert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTariffCodeAlert>%s</%sTariffCodeAlert>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TariffCodeAlert), input_name='TariffCodeAlert')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ProductName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ProductName')
            value_ = self.gds_validate_string(value_, node, 'ProductName')
            self.ProductName = value_
            self.ProductName_nsprefix_ = child_.prefix
        elif nodeName_ == 'ProductDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ProductDescription')
            value_ = self.gds_validate_string(value_, node, 'ProductDescription')
            self.ProductDescription = value_
            self.ProductDescription_nsprefix_ = child_.prefix
        elif nodeName_ == 'ProductCountryCodeOfOrigin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ProductCountryCodeOfOrigin')
            value_ = self.gds_validate_string(value_, node, 'ProductCountryCodeOfOrigin')
            self.ProductCountryCodeOfOrigin = value_
            self.ProductCountryCodeOfOrigin_nsprefix_ = child_.prefix
        elif nodeName_ == 'TariffInfo':
            obj_ = TariffInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TariffInfo = obj_
            obj_.original_tagname_ = 'TariffInfo'
        elif nodeName_ == 'Quantity':
            obj_ = ValueWithUnitsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Quantity = obj_
            obj_.original_tagname_ = 'Quantity'
        elif nodeName_ == 'UnitPrice':
            obj_ = ChargesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnitPrice = obj_
            obj_.original_tagname_ = 'UnitPrice'
        elif nodeName_ == 'Weight':
            obj_ = ValueWithUnitsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Weight = obj_
            obj_.original_tagname_ = 'Weight'
        elif nodeName_ == 'TariffCodeAlert':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TariffCodeAlert')
            value_ = self.gds_validate_string(value_, node, 'TariffCodeAlert')
            self.TariffCodeAlert = value_
            self.TariffCodeAlert_nsprefix_ = child_.prefix
# end class ProductType


class ProductResultType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TariffCode=None, Question=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TariffCode = TariffCode
        self.TariffCode_nsprefix_ = None
        if Question is None:
            self.Question = []
        else:
            self.Question = Question
        self.Question_nsprefix_ = "lc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductResultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductResultType.subclass:
            return ProductResultType.subclass(*args_, **kwargs_)
        else:
            return ProductResultType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TariffCode(self):
        return self.TariffCode
    def set_TariffCode(self, TariffCode):
        self.TariffCode = TariffCode
    def get_Question(self):
        return self.Question
    def set_Question(self, Question):
        self.Question = Question
    def add_Question(self, value):
        self.Question.append(value)
    def insert_Question_at(self, index, value):
        self.Question.insert(index, value)
    def replace_Question_at(self, index, value):
        self.Question[index] = value
    def _hasContent(self):
        if (
            self.TariffCode is not None or
            self.Question
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductResultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductResultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductResultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductResultType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductResultType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductResultType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductResultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TariffCode is not None:
            namespaceprefix_ = self.TariffCode_nsprefix_ + ':' if (UseCapturedNS_ and self.TariffCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTariffCode>%s</%sTariffCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TariffCode), input_name='TariffCode')), namespaceprefix_ , eol_))
        for Question_ in self.Question:
            namespaceprefix_ = self.Question_nsprefix_ + ':' if (UseCapturedNS_ and self.Question_nsprefix_) else ''
            Question_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Question', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TariffCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TariffCode')
            value_ = self.gds_validate_string(value_, node, 'TariffCode')
            self.TariffCode = value_
            self.TariffCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Question':
            obj_ = QuestionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Question.append(obj_)
            obj_.original_tagname_ = 'Question'
# end class ProductResultType


class ProductAnswerType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TariffCode=None, Question=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TariffCode = TariffCode
        self.TariffCode_nsprefix_ = None
        if Question is None:
            self.Question = []
        else:
            self.Question = Question
        self.Question_nsprefix_ = "lc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductAnswerType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductAnswerType.subclass:
            return ProductAnswerType.subclass(*args_, **kwargs_)
        else:
            return ProductAnswerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TariffCode(self):
        return self.TariffCode
    def set_TariffCode(self, TariffCode):
        self.TariffCode = TariffCode
    def get_Question(self):
        return self.Question
    def set_Question(self, Question):
        self.Question = Question
    def add_Question(self, value):
        self.Question.append(value)
    def insert_Question_at(self, index, value):
        self.Question.insert(index, value)
    def replace_Question_at(self, index, value):
        self.Question[index] = value
    def _hasContent(self):
        if (
            self.TariffCode is not None or
            self.Question
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductAnswerType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductAnswerType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductAnswerType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductAnswerType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductAnswerType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductAnswerType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductAnswerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TariffCode is not None:
            namespaceprefix_ = self.TariffCode_nsprefix_ + ':' if (UseCapturedNS_ and self.TariffCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTariffCode>%s</%sTariffCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TariffCode), input_name='TariffCode')), namespaceprefix_ , eol_))
        for Question_ in self.Question:
            namespaceprefix_ = self.Question_nsprefix_ + ':' if (UseCapturedNS_ and self.Question_nsprefix_) else ''
            Question_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Question', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TariffCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TariffCode')
            value_ = self.gds_validate_string(value_, node, 'TariffCode')
            self.TariffCode = value_
            self.TariffCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Question':
            obj_ = AnswerType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Question.append(obj_)
            obj_.original_tagname_ = 'Question'
# end class ProductAnswerType


class ProductsChargesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Product=None, ProductsSubTotal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Product is None:
            self.Product = []
        else:
            self.Product = Product
        self.Product_nsprefix_ = "lc"
        self.ProductsSubTotal = ProductsSubTotal
        self.ProductsSubTotal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductsChargesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductsChargesType.subclass:
            return ProductsChargesType.subclass(*args_, **kwargs_)
        else:
            return ProductsChargesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Product(self):
        return self.Product
    def set_Product(self, Product):
        self.Product = Product
    def add_Product(self, value):
        self.Product.append(value)
    def insert_Product_at(self, index, value):
        self.Product.insert(index, value)
    def replace_Product_at(self, index, value):
        self.Product[index] = value
    def get_ProductsSubTotal(self):
        return self.ProductsSubTotal
    def set_ProductsSubTotal(self, ProductsSubTotal):
        self.ProductsSubTotal = ProductsSubTotal
    def _hasContent(self):
        if (
            self.Product or
            self.ProductsSubTotal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductsChargesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductsChargesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductsChargesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductsChargesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductsChargesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductsChargesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductsChargesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Product_ in self.Product:
            namespaceprefix_ = self.Product_nsprefix_ + ':' if (UseCapturedNS_ and self.Product_nsprefix_) else ''
            Product_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Product', pretty_print=pretty_print)
        if self.ProductsSubTotal is not None:
            namespaceprefix_ = self.ProductsSubTotal_nsprefix_ + ':' if (UseCapturedNS_ and self.ProductsSubTotal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sProductsSubTotal>%s</%sProductsSubTotal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ProductsSubTotal), input_name='ProductsSubTotal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Product':
            obj_ = ProductEstimateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Product.append(obj_)
            obj_.original_tagname_ = 'Product'
        elif nodeName_ == 'ProductsSubTotal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ProductsSubTotal')
            value_ = self.gds_validate_string(value_, node, 'ProductsSubTotal')
            self.ProductsSubTotal = value_
            self.ProductsSubTotal_nsprefix_ = child_.prefix
# end class ProductsChargesType


class ProductEstimateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TariffCode=None, Charges=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TariffCode = TariffCode
        self.TariffCode_nsprefix_ = None
        self.Charges = Charges
        self.Charges_nsprefix_ = "lc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductEstimateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductEstimateType.subclass:
            return ProductEstimateType.subclass(*args_, **kwargs_)
        else:
            return ProductEstimateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TariffCode(self):
        return self.TariffCode
    def set_TariffCode(self, TariffCode):
        self.TariffCode = TariffCode
    def get_Charges(self):
        return self.Charges
    def set_Charges(self, Charges):
        self.Charges = Charges
    def _hasContent(self):
        if (
            self.TariffCode is not None or
            self.Charges is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductEstimateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductEstimateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductEstimateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductEstimateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductEstimateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductEstimateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductEstimateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TariffCode is not None:
            namespaceprefix_ = self.TariffCode_nsprefix_ + ':' if (UseCapturedNS_ and self.TariffCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTariffCode>%s</%sTariffCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TariffCode), input_name='TariffCode')), namespaceprefix_ , eol_))
        if self.Charges is not None:
            namespaceprefix_ = self.Charges_nsprefix_ + ':' if (UseCapturedNS_ and self.Charges_nsprefix_) else ''
            self.Charges.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Charges', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TariffCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TariffCode')
            value_ = self.gds_validate_string(value_, node, 'TariffCode')
            self.TariffCode = value_
            self.TariffCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Charges':
            obj_ = ProductChargesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Charges = obj_
            obj_.original_tagname_ = 'Charges'
# end class ProductEstimateType


class TariffInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TariffCode=None, DetailID=None, SecondaryTariffCode=None, SecondaryDetailID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TariffCode = TariffCode
        self.TariffCode_nsprefix_ = None
        self.DetailID = DetailID
        self.DetailID_nsprefix_ = None
        self.SecondaryTariffCode = SecondaryTariffCode
        self.SecondaryTariffCode_nsprefix_ = None
        self.SecondaryDetailID = SecondaryDetailID
        self.SecondaryDetailID_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TariffInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TariffInfoType.subclass:
            return TariffInfoType.subclass(*args_, **kwargs_)
        else:
            return TariffInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TariffCode(self):
        return self.TariffCode
    def set_TariffCode(self, TariffCode):
        self.TariffCode = TariffCode
    def get_DetailID(self):
        return self.DetailID
    def set_DetailID(self, DetailID):
        self.DetailID = DetailID
    def get_SecondaryTariffCode(self):
        return self.SecondaryTariffCode
    def set_SecondaryTariffCode(self, SecondaryTariffCode):
        self.SecondaryTariffCode = SecondaryTariffCode
    def get_SecondaryDetailID(self):
        return self.SecondaryDetailID
    def set_SecondaryDetailID(self, SecondaryDetailID):
        self.SecondaryDetailID = SecondaryDetailID
    def _hasContent(self):
        if (
            self.TariffCode is not None or
            self.DetailID is not None or
            self.SecondaryTariffCode is not None or
            self.SecondaryDetailID is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TariffInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TariffInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TariffInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TariffInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TariffInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TariffInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TariffInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TariffCode is not None:
            namespaceprefix_ = self.TariffCode_nsprefix_ + ':' if (UseCapturedNS_ and self.TariffCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTariffCode>%s</%sTariffCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TariffCode), input_name='TariffCode')), namespaceprefix_ , eol_))
        if self.DetailID is not None:
            namespaceprefix_ = self.DetailID_nsprefix_ + ':' if (UseCapturedNS_ and self.DetailID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDetailID>%s</%sDetailID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DetailID), input_name='DetailID')), namespaceprefix_ , eol_))
        if self.SecondaryTariffCode is not None:
            namespaceprefix_ = self.SecondaryTariffCode_nsprefix_ + ':' if (UseCapturedNS_ and self.SecondaryTariffCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSecondaryTariffCode>%s</%sSecondaryTariffCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SecondaryTariffCode), input_name='SecondaryTariffCode')), namespaceprefix_ , eol_))
        if self.SecondaryDetailID is not None:
            namespaceprefix_ = self.SecondaryDetailID_nsprefix_ + ':' if (UseCapturedNS_ and self.SecondaryDetailID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSecondaryDetailID>%s</%sSecondaryDetailID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SecondaryDetailID), input_name='SecondaryDetailID')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TariffCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TariffCode')
            value_ = self.gds_validate_string(value_, node, 'TariffCode')
            self.TariffCode = value_
            self.TariffCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'DetailID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DetailID')
            value_ = self.gds_validate_string(value_, node, 'DetailID')
            self.DetailID = value_
            self.DetailID_nsprefix_ = child_.prefix
        elif nodeName_ == 'SecondaryTariffCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SecondaryTariffCode')
            value_ = self.gds_validate_string(value_, node, 'SecondaryTariffCode')
            self.SecondaryTariffCode = value_
            self.SecondaryTariffCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'SecondaryDetailID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SecondaryDetailID')
            value_ = self.gds_validate_string(value_, node, 'SecondaryDetailID')
            self.SecondaryDetailID = value_
            self.SecondaryDetailID_nsprefix_ = child_.prefix
# end class TariffInfoType


class ValueWithUnitsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Value=None, UnitOfMeasure=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
        self.UnitOfMeasure = UnitOfMeasure
        self.UnitOfMeasure_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ValueWithUnitsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ValueWithUnitsType.subclass:
            return ValueWithUnitsType.subclass(*args_, **kwargs_)
        else:
            return ValueWithUnitsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_UnitOfMeasure(self):
        return self.UnitOfMeasure
    def set_UnitOfMeasure(self, UnitOfMeasure):
        self.UnitOfMeasure = UnitOfMeasure
    def _hasContent(self):
        if (
            self.Value is not None or
            self.UnitOfMeasure is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ValueWithUnitsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ValueWithUnitsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ValueWithUnitsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ValueWithUnitsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ValueWithUnitsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ValueWithUnitsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ValueWithUnitsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
        if self.UnitOfMeasure is not None:
            namespaceprefix_ = self.UnitOfMeasure_nsprefix_ + ':' if (UseCapturedNS_ and self.UnitOfMeasure_nsprefix_) else ''
            self.UnitOfMeasure.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnitOfMeasure', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
        elif nodeName_ == 'UnitOfMeasure':
            obj_ = UnitOfMeasureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnitOfMeasure = obj_
            obj_.original_tagname_ = 'UnitOfMeasure'
# end class ValueWithUnitsType


class ChargesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, MonetaryValue=None, CurrencyCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.MonetaryValue = MonetaryValue
        self.MonetaryValue_nsprefix_ = None
        self.CurrencyCode = CurrencyCode
        self.CurrencyCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChargesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChargesType.subclass:
            return ChargesType.subclass(*args_, **kwargs_)
        else:
            return ChargesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MonetaryValue(self):
        return self.MonetaryValue
    def set_MonetaryValue(self, MonetaryValue):
        self.MonetaryValue = MonetaryValue
    def get_CurrencyCode(self):
        return self.CurrencyCode
    def set_CurrencyCode(self, CurrencyCode):
        self.CurrencyCode = CurrencyCode
    def _hasContent(self):
        if (
            self.MonetaryValue is not None or
            self.CurrencyCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ChargesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChargesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChargesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChargesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChargesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ChargesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.MonetaryValue is not None:
            namespaceprefix_ = self.MonetaryValue_nsprefix_ + ':' if (UseCapturedNS_ and self.MonetaryValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMonetaryValue>%s</%sMonetaryValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MonetaryValue), input_name='MonetaryValue')), namespaceprefix_ , eol_))
        if self.CurrencyCode is not None:
            namespaceprefix_ = self.CurrencyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CurrencyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCurrencyCode>%s</%sCurrencyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CurrencyCode), input_name='CurrencyCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MonetaryValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MonetaryValue')
            value_ = self.gds_validate_string(value_, node, 'MonetaryValue')
            self.MonetaryValue = value_
            self.MonetaryValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'CurrencyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CurrencyCode')
            value_ = self.gds_validate_string(value_, node, 'CurrencyCode')
            self.CurrencyCode = value_
            self.CurrencyCode_nsprefix_ = child_.prefix
# end class ChargesType


class QuestionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Text=None, Type=None, Options=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Text = Text
        self.Text_nsprefix_ = None
        self.Type = Type
        self.Type_nsprefix_ = None
        self.Options = Options
        self.Options_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QuestionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QuestionType.subclass:
            return QuestionType.subclass(*args_, **kwargs_)
        else:
            return QuestionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Text(self):
        return self.Text
    def set_Text(self, Text):
        self.Text = Text
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def get_Options(self):
        return self.Options
    def set_Options(self, Options):
        self.Options = Options
    def _hasContent(self):
        if (
            self.Name is not None or
            self.Text is not None or
            self.Type is not None or
            self.Options is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='QuestionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QuestionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QuestionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QuestionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QuestionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QuestionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='QuestionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            namespaceprefix_ = self.Name_nsprefix_ + ':' if (UseCapturedNS_ and self.Name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sName>%s</%sName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Name), input_name='Name')), namespaceprefix_ , eol_))
        if self.Text is not None:
            namespaceprefix_ = self.Text_nsprefix_ + ':' if (UseCapturedNS_ and self.Text_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sText>%s</%sText>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Text), input_name='Text')), namespaceprefix_ , eol_))
        if self.Type is not None:
            namespaceprefix_ = self.Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sType>%s</%sType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Type), input_name='Type')), namespaceprefix_ , eol_))
        if self.Options is not None:
            namespaceprefix_ = self.Options_nsprefix_ + ':' if (UseCapturedNS_ and self.Options_nsprefix_) else ''
            self.Options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Options', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Name')
            value_ = self.gds_validate_string(value_, node, 'Name')
            self.Name = value_
            self.Name_nsprefix_ = child_.prefix
        elif nodeName_ == 'Text':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Text')
            value_ = self.gds_validate_string(value_, node, 'Text')
            self.Text = value_
            self.Text_nsprefix_ = child_.prefix
        elif nodeName_ == 'Type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Type')
            value_ = self.gds_validate_string(value_, node, 'Type')
            self.Type = value_
            self.Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Options':
            obj_ = OptionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Options = obj_
            obj_.original_tagname_ = 'Options'
# end class QuestionType


class KeyValuePairType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Key=None, Value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Key = Key
        self.Key_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyValuePairType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyValuePairType.subclass:
            return KeyValuePairType.subclass(*args_, **kwargs_)
        else:
            return KeyValuePairType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Key(self):
        return self.Key
    def set_Key(self, Key):
        self.Key = Key
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def _hasContent(self):
        if (
            self.Key is not None or
            self.Value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='KeyValuePairType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyValuePairType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyValuePairType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyValuePairType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyValuePairType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='KeyValuePairType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='KeyValuePairType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Key is not None:
            namespaceprefix_ = self.Key_nsprefix_ + ':' if (UseCapturedNS_ and self.Key_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sKey>%s</%sKey>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Key), input_name='Key')), namespaceprefix_ , eol_))
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Key':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Key')
            value_ = self.gds_validate_string(value_, node, 'Key')
            self.Key = value_
            self.Key_nsprefix_ = child_.prefix
        elif nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
# end class KeyValuePairType


class AnswerType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Answer=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Answer = Answer
        self.Answer_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AnswerType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AnswerType.subclass:
            return AnswerType.subclass(*args_, **kwargs_)
        else:
            return AnswerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Answer(self):
        return self.Answer
    def set_Answer(self, Answer):
        self.Answer = Answer
    def _hasContent(self):
        if (
            self.Name is not None or
            self.Answer is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AnswerType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AnswerType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AnswerType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AnswerType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AnswerType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AnswerType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AnswerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            namespaceprefix_ = self.Name_nsprefix_ + ':' if (UseCapturedNS_ and self.Name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sName>%s</%sName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Name), input_name='Name')), namespaceprefix_ , eol_))
        if self.Answer is not None:
            namespaceprefix_ = self.Answer_nsprefix_ + ':' if (UseCapturedNS_ and self.Answer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAnswer>%s</%sAnswer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Answer), input_name='Answer')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Name')
            value_ = self.gds_validate_string(value_, node, 'Name')
            self.Name = value_
            self.Name_nsprefix_ = child_.prefix
        elif nodeName_ == 'Answer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Answer')
            value_ = self.gds_validate_string(value_, node, 'Answer')
            self.Answer = value_
            self.Answer_nsprefix_ = child_.prefix
# end class AnswerType


class ProductChargesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Duties=None, TaxesAndFees=None, VAT=None, CostOfGoods=None, SubTotal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Duties = Duties
        self.Duties_nsprefix_ = None
        self.TaxesAndFees = TaxesAndFees
        self.TaxesAndFees_nsprefix_ = None
        self.VAT = VAT
        self.VAT_nsprefix_ = None
        self.CostOfGoods = CostOfGoods
        self.CostOfGoods_nsprefix_ = None
        self.SubTotal = SubTotal
        self.SubTotal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductChargesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductChargesType.subclass:
            return ProductChargesType.subclass(*args_, **kwargs_)
        else:
            return ProductChargesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Duties(self):
        return self.Duties
    def set_Duties(self, Duties):
        self.Duties = Duties
    def get_TaxesAndFees(self):
        return self.TaxesAndFees
    def set_TaxesAndFees(self, TaxesAndFees):
        self.TaxesAndFees = TaxesAndFees
    def get_VAT(self):
        return self.VAT
    def set_VAT(self, VAT):
        self.VAT = VAT
    def get_CostOfGoods(self):
        return self.CostOfGoods
    def set_CostOfGoods(self, CostOfGoods):
        self.CostOfGoods = CostOfGoods
    def get_SubTotal(self):
        return self.SubTotal
    def set_SubTotal(self, SubTotal):
        self.SubTotal = SubTotal
    def _hasContent(self):
        if (
            self.Duties is not None or
            self.TaxesAndFees is not None or
            self.VAT is not None or
            self.CostOfGoods is not None or
            self.SubTotal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductChargesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductChargesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductChargesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductChargesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductChargesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductChargesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ProductChargesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Duties is not None:
            namespaceprefix_ = self.Duties_nsprefix_ + ':' if (UseCapturedNS_ and self.Duties_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDuties>%s</%sDuties>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Duties), input_name='Duties')), namespaceprefix_ , eol_))
        if self.TaxesAndFees is not None:
            namespaceprefix_ = self.TaxesAndFees_nsprefix_ + ':' if (UseCapturedNS_ and self.TaxesAndFees_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTaxesAndFees>%s</%sTaxesAndFees>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TaxesAndFees), input_name='TaxesAndFees')), namespaceprefix_ , eol_))
        if self.VAT is not None:
            namespaceprefix_ = self.VAT_nsprefix_ + ':' if (UseCapturedNS_ and self.VAT_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVAT>%s</%sVAT>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.VAT), input_name='VAT')), namespaceprefix_ , eol_))
        if self.CostOfGoods is not None:
            namespaceprefix_ = self.CostOfGoods_nsprefix_ + ':' if (UseCapturedNS_ and self.CostOfGoods_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCostOfGoods>%s</%sCostOfGoods>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CostOfGoods), input_name='CostOfGoods')), namespaceprefix_ , eol_))
        if self.SubTotal is not None:
            namespaceprefix_ = self.SubTotal_nsprefix_ + ':' if (UseCapturedNS_ and self.SubTotal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSubTotal>%s</%sSubTotal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SubTotal), input_name='SubTotal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Duties':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Duties')
            value_ = self.gds_validate_string(value_, node, 'Duties')
            self.Duties = value_
            self.Duties_nsprefix_ = child_.prefix
        elif nodeName_ == 'TaxesAndFees':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TaxesAndFees')
            value_ = self.gds_validate_string(value_, node, 'TaxesAndFees')
            self.TaxesAndFees = value_
            self.TaxesAndFees_nsprefix_ = child_.prefix
        elif nodeName_ == 'VAT':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'VAT')
            value_ = self.gds_validate_string(value_, node, 'VAT')
            self.VAT = value_
            self.VAT_nsprefix_ = child_.prefix
        elif nodeName_ == 'CostOfGoods':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CostOfGoods')
            value_ = self.gds_validate_string(value_, node, 'CostOfGoods')
            self.CostOfGoods = value_
            self.CostOfGoods_nsprefix_ = child_.prefix
        elif nodeName_ == 'SubTotal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SubTotal')
            value_ = self.gds_validate_string(value_, node, 'SubTotal')
            self.SubTotal = value_
            self.SubTotal_nsprefix_ = child_.prefix
# end class ProductChargesType


class ShipmentChargesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TaxesAndFees=None, AdditionalInsuranceCost=None, TransportationCost=None, SubTotal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TaxesAndFees = TaxesAndFees
        self.TaxesAndFees_nsprefix_ = None
        self.AdditionalInsuranceCost = AdditionalInsuranceCost
        self.AdditionalInsuranceCost_nsprefix_ = None
        self.TransportationCost = TransportationCost
        self.TransportationCost_nsprefix_ = None
        self.SubTotal = SubTotal
        self.SubTotal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentChargesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentChargesType.subclass:
            return ShipmentChargesType.subclass(*args_, **kwargs_)
        else:
            return ShipmentChargesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TaxesAndFees(self):
        return self.TaxesAndFees
    def set_TaxesAndFees(self, TaxesAndFees):
        self.TaxesAndFees = TaxesAndFees
    def get_AdditionalInsuranceCost(self):
        return self.AdditionalInsuranceCost
    def set_AdditionalInsuranceCost(self, AdditionalInsuranceCost):
        self.AdditionalInsuranceCost = AdditionalInsuranceCost
    def get_TransportationCost(self):
        return self.TransportationCost
    def set_TransportationCost(self, TransportationCost):
        self.TransportationCost = TransportationCost
    def get_SubTotal(self):
        return self.SubTotal
    def set_SubTotal(self, SubTotal):
        self.SubTotal = SubTotal
    def _hasContent(self):
        if (
            self.TaxesAndFees is not None or
            self.AdditionalInsuranceCost is not None or
            self.TransportationCost is not None or
            self.SubTotal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentChargesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentChargesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentChargesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentChargesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentChargesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentChargesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentChargesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TaxesAndFees is not None:
            namespaceprefix_ = self.TaxesAndFees_nsprefix_ + ':' if (UseCapturedNS_ and self.TaxesAndFees_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTaxesAndFees>%s</%sTaxesAndFees>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TaxesAndFees), input_name='TaxesAndFees')), namespaceprefix_ , eol_))
        if self.AdditionalInsuranceCost is not None:
            namespaceprefix_ = self.AdditionalInsuranceCost_nsprefix_ + ':' if (UseCapturedNS_ and self.AdditionalInsuranceCost_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAdditionalInsuranceCost>%s</%sAdditionalInsuranceCost>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AdditionalInsuranceCost), input_name='AdditionalInsuranceCost')), namespaceprefix_ , eol_))
        if self.TransportationCost is not None:
            namespaceprefix_ = self.TransportationCost_nsprefix_ + ':' if (UseCapturedNS_ and self.TransportationCost_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransportationCost>%s</%sTransportationCost>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TransportationCost), input_name='TransportationCost')), namespaceprefix_ , eol_))
        if self.SubTotal is not None:
            namespaceprefix_ = self.SubTotal_nsprefix_ + ':' if (UseCapturedNS_ and self.SubTotal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSubTotal>%s</%sSubTotal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SubTotal), input_name='SubTotal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TaxesAndFees':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TaxesAndFees')
            value_ = self.gds_validate_string(value_, node, 'TaxesAndFees')
            self.TaxesAndFees = value_
            self.TaxesAndFees_nsprefix_ = child_.prefix
        elif nodeName_ == 'AdditionalInsuranceCost':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AdditionalInsuranceCost')
            value_ = self.gds_validate_string(value_, node, 'AdditionalInsuranceCost')
            self.AdditionalInsuranceCost = value_
            self.AdditionalInsuranceCost_nsprefix_ = child_.prefix
        elif nodeName_ == 'TransportationCost':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransportationCost')
            value_ = self.gds_validate_string(value_, node, 'TransportationCost')
            self.TransportationCost = value_
            self.TransportationCost_nsprefix_ = child_.prefix
        elif nodeName_ == 'SubTotal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SubTotal')
            value_ = self.gds_validate_string(value_, node, 'SubTotal')
            self.SubTotal = value_
            self.SubTotal_nsprefix_ = child_.prefix
# end class ShipmentChargesType


class TransactionChargeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, MonetaryValue=None, CurrencyCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.MonetaryValue = MonetaryValue
        self.MonetaryValue_nsprefix_ = None
        self.CurrencyCode = CurrencyCode
        self.CurrencyCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransactionChargeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransactionChargeType.subclass:
            return TransactionChargeType.subclass(*args_, **kwargs_)
        else:
            return TransactionChargeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MonetaryValue(self):
        return self.MonetaryValue
    def set_MonetaryValue(self, MonetaryValue):
        self.MonetaryValue = MonetaryValue
    def get_CurrencyCode(self):
        return self.CurrencyCode
    def set_CurrencyCode(self, CurrencyCode):
        self.CurrencyCode = CurrencyCode
    def _hasContent(self):
        if (
            self.MonetaryValue is not None or
            self.CurrencyCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TransactionChargeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransactionChargeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransactionChargeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransactionChargeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransactionChargeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TransactionChargeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TransactionChargeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.MonetaryValue is not None:
            namespaceprefix_ = self.MonetaryValue_nsprefix_ + ':' if (UseCapturedNS_ and self.MonetaryValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMonetaryValue>%s</%sMonetaryValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MonetaryValue), input_name='MonetaryValue')), namespaceprefix_ , eol_))
        if self.CurrencyCode is not None:
            namespaceprefix_ = self.CurrencyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CurrencyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCurrencyCode>%s</%sCurrencyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CurrencyCode), input_name='CurrencyCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MonetaryValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MonetaryValue')
            value_ = self.gds_validate_string(value_, node, 'MonetaryValue')
            self.MonetaryValue = value_
            self.MonetaryValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'CurrencyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CurrencyCode')
            value_ = self.gds_validate_string(value_, node, 'CurrencyCode')
            self.CurrencyCode = value_
            self.CurrencyCode_nsprefix_ = child_.prefix
# end class TransactionChargeType


class UnitOfMeasureType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, UnitCode=None, UnitDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.UnitCode = UnitCode
        self.UnitCode_nsprefix_ = None
        self.UnitDescription = UnitDescription
        self.UnitDescription_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UnitOfMeasureType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UnitOfMeasureType.subclass:
            return UnitOfMeasureType.subclass(*args_, **kwargs_)
        else:
            return UnitOfMeasureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UnitCode(self):
        return self.UnitCode
    def set_UnitCode(self, UnitCode):
        self.UnitCode = UnitCode
    def get_UnitDescription(self):
        return self.UnitDescription
    def set_UnitDescription(self, UnitDescription):
        self.UnitDescription = UnitDescription
    def _hasContent(self):
        if (
            self.UnitCode is not None or
            self.UnitDescription is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='UnitOfMeasureType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UnitOfMeasureType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UnitOfMeasureType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UnitOfMeasureType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UnitOfMeasureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UnitOfMeasureType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='UnitOfMeasureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.UnitCode is not None:
            namespaceprefix_ = self.UnitCode_nsprefix_ + ':' if (UseCapturedNS_ and self.UnitCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUnitCode>%s</%sUnitCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.UnitCode), input_name='UnitCode')), namespaceprefix_ , eol_))
        if self.UnitDescription is not None:
            namespaceprefix_ = self.UnitDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.UnitDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUnitDescription>%s</%sUnitDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.UnitDescription), input_name='UnitDescription')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UnitCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'UnitCode')
            value_ = self.gds_validate_string(value_, node, 'UnitCode')
            self.UnitCode = value_
            self.UnitCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'UnitDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'UnitDescription')
            value_ = self.gds_validate_string(value_, node, 'UnitDescription')
            self.UnitDescription = value_
            self.UnitDescription_nsprefix_ = child_.prefix
# end class UnitOfMeasureType


class OptionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Option=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Option is None:
            self.Option = []
        else:
            self.Option = Option
        self.Option_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OptionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OptionsType.subclass:
            return OptionsType.subclass(*args_, **kwargs_)
        else:
            return OptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Option(self):
        return self.Option
    def set_Option(self, Option):
        self.Option = Option
    def add_Option(self, value):
        self.Option.append(value)
    def insert_Option_at(self, index, value):
        self.Option.insert(index, value)
    def replace_Option_at(self, index, value):
        self.Option[index] = value
    def _hasContent(self):
        if (
            self.Option
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OptionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OptionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OptionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OptionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OptionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OptionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Option_ in self.Option:
            namespaceprefix_ = self.Option_nsprefix_ + ':' if (UseCapturedNS_ and self.Option_nsprefix_) else ''
            Option_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Option', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Option':
            obj_ = KeyValuePairType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Option.append(obj_)
            obj_.original_tagname_ = 'Option'
# end class OptionsType


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
        rootTag = 'LandedCostRequest'
        rootClass = LandedCostRequest
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
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'LandedCostRequest'
        rootClass = LandedCostRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
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
    return rootObj, rootElement, mapping, reverse_node_mapping


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
        rootTag = 'LandedCostRequest'
        rootClass = LandedCostRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:lc="http://www.ups.com/schema/xpci/1.0/lc"')
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
        rootTag = 'LandedCostRequest'
        rootClass = LandedCostRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from landed_cost_web_service_schema import *\n\n')
        sys.stdout.write('import landed_cost_web_service_schema as model_\n\n')
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
NamespaceToDefMappings_ = {'http://www.ups.com/schema/xpci/1.0/lc': [('RequestTransportType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('QueryRequestType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('EstimateRequestType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ResponseTransportType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('QueryResponseType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('EstimateResponseType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ShipmentType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ShipmentResultType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ShipmentAnswerType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ShipmentEstimateType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('TransactionInfoType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ProductType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ProductResultType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ProductAnswerType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ProductsChargesType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ProductEstimateType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('TariffInfoType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ValueWithUnitsType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ChargesType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('QuestionType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('KeyValuePairType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('AnswerType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ProductChargesType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT'),
                                           ('ShipmentChargesType',
                                            './schemas/LandedCostWebServiceSchema.xsd',
                                            'CT')]}

__all__ = [
    "AnswerType",
    "ChargesType",
    "EstimateRequestType",
    "EstimateResponseType",
    "KeyValuePairType",
    "LandedCostRequest",
    "LandedCostResponse",
    "OptionsType",
    "ProductAnswerType",
    "ProductChargesType",
    "ProductEstimateType",
    "ProductResultType",
    "ProductType",
    "ProductsChargesType",
    "QueryRequestType",
    "QueryResponseType",
    "QuestionType",
    "RequestTransportType",
    "ResponseTransportType",
    "ShipmentAnswerType",
    "ShipmentChargesType",
    "ShipmentEstimateType",
    "ShipmentResultType",
    "ShipmentType",
    "TariffInfoType",
    "TransactionChargeType",
    "TransactionInfoType",
    "UnitOfMeasureType",
    "ValueWithUnitsType"
]
