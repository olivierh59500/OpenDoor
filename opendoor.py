#! /usr/bin/env python

""" OWASP OpenDoor launcher """

#    OpenDoor Web Directory Scanner
#    Copyright (C) 2016  Stanislav Menshov
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Development Team: Stanislav Menshov
#

try:
    import urllib3
    import threadpool
    import linereader
    import colorama
    import coloredlogs
    import termcolor
    import logging
    import verboselogs
    import tabulate

except ImportError:
    exit("""\t\t[!] Several dependencies wasn't installed!
                Please run sudo pip install -r requirements.txt """)

if __name__ == "__main__":
    from Libraries.Command import Command
    from Libraries.Controller import Controller
    from Libraries.Version import Version
    from Libraries.Filter import Filter as FilterArgs

    version = Version()
    command = Command()
    filter_args = FilterArgs()
    args_values = command.get_arg_values()
    args = []

    version.banner()

    if args_values:
        args = filter_args.call(command)
        Controller(args)
