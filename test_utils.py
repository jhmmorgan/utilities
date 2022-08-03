import pytest

from utils import _terminal_output
from utils import print2


class Test_TerminalOutput(object):
    def err_message(self, name, actual, expected):
        return f"fun .{name} should return {repr(expected)}, but returned {repr(actual)}!"

    # Fill in with the correct mandatory argument
    _new_style_tests = [
        ["1",       "\033[1m"],
        [("1", "2"), "\033[1;2m"]
    ]
    @pytest.mark.parametrize("input, expected", _new_style_tests)
    def test_on_new_style(self, input, expected):
        actual = _terminal_output.new_style(input)
        assert repr(expected) == repr(actual), self.err_message("new_style", actual, expected)

    def test_on_end_style(self):
        expected = "\033[0m"
        actual   = _terminal_output.end_style()
        assert repr(expected) == repr(actual), self.err_message("end_style", actual, expected)

    __join_tests = [
        [["1", "2"],    "1;2"],
        [("3", "4"),    "3;4"]
    ]
    @pytest.mark.parametrize("input, expected", __join_tests)
    def test_on__join(self, input, expected):
        actual = _terminal_output._join(input)
        assert repr(expected) == repr(actual), self.err_message("_join", actual, expected)


    _create_style_tests = [
        ["1", "test_message", True,                      "\033[1m" + "test_message" + "\033[0m"],
        [("1", "4", "30", "46"), "test_message", True,   "\033[1;4;30;46m" + "test_message" + "\033[0m"],
        ["30", "test_message", False,                    "\033[30m" + "test_message"]
    ]
    @pytest.mark.parametrize("style, message, ending, expected", _create_style_tests)
    def test_on_create_style(self, style, message, ending, expected):
        actual = _terminal_output.create_style(style, message, ending)
        assert repr(expected) == repr(actual), self.err_message("create_style", actual, expected)  


class Test_Print2(object):
    def err_message(self, name, actual, expected):
        return f"fun .{name} should return {repr(expected)}, but returned {repr(actual)}!"

    # Fill in with the correct mandatory argument
    _print_tests = [
        ["test_message", "1", True, True, "\n",             "\033[1m"    + "test_message" + "\033[0m"],
        ["test_message", ("1", "30"), True, True, "\n",     "\033[1;30m" + "test_message" + "\033[0m"],
        ["test_message", "1", False, False, "\n",           None],
        ["test_message", ("1", "30"), False, False, "\n",   None]
    ]
    @pytest.mark.parametrize("string, style, _print, _return, end, expected", _print_tests)
    def test_on_print(self, string, style, _print, _return, end, expected):
        actual = print2.print(string, style, _print = _print, _return = _return, end = end)
        assert repr(expected) == repr(actual), self.err_message("print", actual, expected)


    _bold_tests = [
        ["first_message", True,           "\033[1m"    + "first_message"  + "\033[0m"],
        ["second_message", True,          "\033[1m"    + "second_message" + "\033[0m"],
        ["first_message", False,          None],
        ["second_message", False,         None],
    ]
    @pytest.mark.parametrize("input, _return, expected", _bold_tests)
    def test_on_bold(self, input, _return, expected):
        actual = print2.bold(input, _print = False, _return = _return)
        assert repr(expected) == repr(actual), self.err_message("bold", actual, expected)

