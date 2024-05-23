s = """FAILED test_public.py::test_all_cases[simple] - AssertionError: assert '' == '17\n'
FAILED test_public.py::test_all_cases[globals] - AssertionError: assert 'Pre: 2106\n' == 'Pre: 2106\nMidst: 2107\nPost: 2107\n'
FAILED test_public.py::test_all_cases[for_loop] - AssertionError: assert '' == '01234\n'
FAILED test_public.py::test_all_cases[generator_expression_in_join] - AssertionError: assert '' == 'Assert test case for generator_expression_in_join\n'
FAILED test_public.py::test_all_cases[generator_expression_complex] - AssertionError: assert '' == '    test_str\n'
FAILED test_public.py::test_all_cases[list_comprehension] - AssertionError: assert '' == 'Assert test case for list_comprehension\n'
FAILED test_public.py::test_all_cases[dict_comprehension] - AssertionError: assert '' == 'Assert test case for dict_comprehension\n'
FAILED test_public.py::test_all_cases[set_comprehension] - AssertionError: assert '' == 'Assert test case for set_comprehension\n'
FAILED test_public.py::test_all_cases[strange_sequence_ops] - AssertionError: assert '' == 'Assert test case for strange_sequence_ops\n'
FAILED test_public.py::test_all_cases[deleting_names] - AssertionError: assert <class 'AttributeError'> == <class 'NameError'>
FAILED test_public.py::test_all_cases[deleting_local_names] - AssertionError: assert <class 'IndexError'> == <class 'UnboundLocalError'>
FAILED test_public.py::test_all_cases[import] - AssertionError: assert '' == '3.141592653589793 2.718281828459045\n1.4142135623730951\n0.9092974268256817\n'
FAILED test_public.py::test_all_cases[classes] - AssertionError: assert '' == '2 3\n8 15\n'
FAILED test_public.py::test_all_cases[calling_methods_wrong] - AssertionError: assert <class 'AttributeError'> == <class 'TypeError'>
FAILED test_public.py::test_all_cases[calling_subclass_methods] - AssertionError: assert '' == '17\n'
FAILED test_public.py::test_all_cases[subclass_attribute] - AssertionError: assert '' == '17\n'
FAILED test_public.py::test_all_cases[subclass_attributes_not_shared] - AssertionError: assert '' == 'Assert test case for subclass_attributes_not_shared\n'
FAILED test_public.py::test_all_cases[data_descriptors_precede_instance_attributes] - AssertionError: assert '' == 'Assert test case for data_descriptors_precede_instance_attributes\n'
FAILED test_public.py::test_all_cases[instance_attrs_precede_non_data_descriptors] - AssertionError: assert '' == 'Assert test case for instance_attrs_precede_non_data_descriptors\n'
FAILED test_public.py::test_all_cases[subclass_attributes_dynamic] - AssertionError: assert '' == 'Assert test case for subclass_attributes_dynamic\n'
FAILED test_public.py::test_all_cases[attribute_access] - AssertionError: assert '' == '17\n17\n23\n'
FAILED test_public.py::test_all_cases[staticmethods] - AssertionError: assert '' == '1492\n1776\n'
FAILED test_public.py::test_all_cases[unbound_methods] - AssertionError: assert '' == '1815\n'
FAILED test_public.py::test_all_cases[bound_methods] - AssertionError: assert '' == '1815\n'
FAILED test_public.py::test_all_cases[decorator] - AssertionError: assert '' == 'Test case decorator\n'
FAILED test_public.py::test_all_cases[multiple_classes] - AssertionError: assert '' == '6\n7\n'
FAILED test_public.py::test_all_cases[for] - AssertionError: assert '' == '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\ndone\n'
FAILED test_public.py::test_all_cases[break] - AssertionError: assert '' == '0\n1\n2\n3\n4\n5\n6\n7\ndone\n'
FAILED test_public.py::test_all_cases[continue] - AssertionError: assert '' == '1\n2\n4\n5\n7\n8\ndone\n'
FAILED test_public.py::test_all_cases[continue_in_try_except] - AssertionError: assert '' == '1\n2\n4\n5\n7\n8\ndone\n'
FAILED test_public.py::test_all_cases[continue_in_try_finally] - AssertionError: assert '' == '.\n1\n.\n2\n.\n.\n4\n.\n5\n.\n.\n7\n.\n8\n.\n.\ndone\n'
FAILED test_public.py::test_all_cases[nested_names] - AssertionError: assert '' == '2\n1\n'
FAILED test_public.py::test_all_cases[calling_functions_with_args_kwargs] - AssertionError: assert '6 77 88 [99]\n' == '6 77 88 [99]\n7 17 23 [99, 99]\n6 77 23 [123, 99]\n'
FAILED test_public.py::test_all_cases[defining_functions_with_args] - AssertionError: assert '' == 'args is (1, 2)\n'
FAILED test_public.py::test_all_cases[defining_functions_with_kwargs] - assert '' == "kwargs is [('blue', False), ('red', True)]\n"
FAILED test_public.py::test_all_cases[defining_functions_with_args_kwargs] - assert '' == "args is (1, 2)\nkwargs is [('blue', False), ('red', True)]\n"
FAILED test_public.py::test_all_cases[defining_functions_with_keyword_only] - AssertionError: assert '' == 'x is 1, y is 2\n'
FAILED test_public.py::test_all_cases[defining_functions_with_empty_args] - AssertionError: assert '' == 'args is ()\n'
FAILED test_public.py::test_all_cases[defining_functions_with_empty_kwargs] - AssertionError: assert '' == 'kwargs is []\n'
FAILED test_public.py::test_all_cases[defining_functions_with_empty_args_kwargs] - AssertionError: assert '' == 'args is (), kwargs is {}\n'
FAILED test_public.py::test_all_cases[partial] - AssertionError: assert '' == 'Assert test case for partial\n'
FAILED test_public.py::test_all_cases[partial_with_kwargs] - AssertionError: assert '' == 'Assert test case for partial_with_kwargs\n'
FAILED test_public.py::test_all_cases[wraps] - AssertionError: assert '' == 'Calling decorated function\nAssert test case for wraps\n'
FAILED test_public.py::test_all_cases[closures] - AssertionError: assert '' == '17\nAssert test case for closures\n'
FAILED test_public.py::test_all_cases[closures_store_deref] - AssertionError: assert '' == '28\nAssert test case for closures_store_deref\n'
FAILED test_public.py::test_all_cases[closures_in_loop] - AssertionError: assert '' == '0\n1\n2\nAssert test case for closures_in_loop\n'
FAILED test_public.py::test_all_cases[closures_with_defaults] - AssertionError: assert '' == '88\nAssert test case for closures_with_defaults\n'
FAILED test_public.py::test_all_cases[deep_closures] - AssertionError: assert '' == '54\nAssert test case for deep_closures\n'
FAILED test_public.py::test_all_cases[first] - AssertionError: assert '' == '1\n2\n'
FAILED test_public.py::test_all_cases[partial_generator] - AssertionError: assert '' == 'Assert test case for partial_generator\n'
FAILED test_public.py::test_all_cases[yield_multiple_values] - AssertionError: assert '' == '1 2 3\n4 5 6\n'
FAILED test_public.py::test_all_cases[simple_generator] - AssertionError: assert '' == '[0, 1, 2]\n'
FAILED test_public.py::test_all_cases[generator_from_generator] - AssertionError: assert '' == '[1, 2, 5, 10, 17]\n'
FAILED test_public.py::test_all_cases[generator_from_generator2] - assert '' == "[('abc', 'ABC'), ('def', 'DEF')]\n"
FAILED test_public.py::test_all_cases[yield_from] - AssertionError: assert '' == 'Hello, World\n'
FAILED test_public.py::test_all_cases[yield_from_tuple] - AssertionError: assert '' == '1\n2\n3\n4\n'
FAILED test_public.py::test_all_cases[generator] - AssertionError: assert '' == 'Test case generator\n'
FAILED test_public.py::test_all_cases[distinguish_iterators_and_generators] - AssertionError: assert '' == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'
FAILED test_public.py::test_all_cases[nested_yield_from] - AssertionError: assert '' == 'Hello, World\n'
FAILED test_public.py::test_all_cases[return_from_generator] - AssertionError: assert '' == '1\n2\n'
FAILED test_public.py::test_all_cases[return_from_generator_with_yield_from] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[test27] - AssertionError: assert '' == '2\n'
FAILED test_public.py::test_all_cases[test38] - AssertionError: assert '' == '5\n'
FAILED test_public.py::test_all_cases[test47] - AssertionError: assert '' == '100\n'
FAILED test_public.py::test_all_cases[test49] - AssertionError: assert '' == '100\n'
FAILED test_public.py::test_all_cases[test50] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[test53] - AssertionError: assert '' == '6\n'
FAILED test_public.py::test_all_cases[test54] - AssertionError: assert '' == '5\n'
FAILED test_public.py::test_all_cases[test55] - AssertionError: assert '' == '1\n2\n3\n'
FAILED test_public.py::test_all_cases[test56] - AssertionError: assert '' == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n'
FAILED test_public.py::test_all_cases[test57] - AssertionError: assert '' == '[1, 3, 5, 7, 9]\n'
FAILED test_public.py::test_all_cases[test58] - AssertionError: assert '' == '[1, 9, 25, 49, 81]\n'
FAILED test_public.py::test_all_cases[test60] - AssertionError: assert '' == '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
FAILED test_public.py::test_all_cases[test61] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[test62] - AssertionError: assert '' == '30\n'
FAILED test_public.py::test_all_cases[test63] - AssertionError: assert '' == '110\n'
FAILED test_public.py::test_all_cases[test64] - AssertionError: assert '' == '100010\n'
FAILED test_public.py::test_all_cases[test73] - AssertionError: assert '' == '1\n2\n3\n'
FAILED test_public.py::test_all_cases[test76] - AssertionError: assert '' == '1\n2\n3\n'
FAILED test_public.py::test_all_cases[test77] - AssertionError: assert '' == '1\n2\n4\n5\n7\n8\nfinished\n'
FAILED test_public.py::test_all_cases[test103] - AssertionError: assert '' == '42, does it mean something?\n'
FAILED test_public.py::test_all_cases[simple_context_manager] - assert '' == "Look: 'iwoeiwoeiwoer'\n"
FAILED test_public.py::test_all_cases[raise_in_context_manager] - assert '' == "Look: 'iwoxr'\n"
FAILED test_public.py::test_all_cases[suppressed_raise_in_context_manager] - assert '' == "Look: 'iwoer'\n"
FAILED test_public.py::test_all_cases[return_in_with] - assert '' == "Look: 'iwor'\n"
FAILED test_public.py::test_all_cases[continue_in_with] - assert '' == "Look: 'iwzoeiwoiwzoer'\n"
FAILED test_public.py::test_all_cases[break_in_with] - assert '' == "Look: 'iwzoeiwor'\n"
FAILED test_public.py::test_all_cases[raise_in_with] - assert '' == "Look: 'iwoxr'\n"
FAILED test_public.py::test_all_cases[at_context_manager_simplified] - AssertionError: assert '' == 'Assert test case for at_context_manager_simplified\n'
FAILED test_public.py::test_all_cases[at_context_manager_complete] - AssertionError: assert '' == 'Assert test case for at_context_manager_complete\n'
FAILED test_public.py::test_all_cases[generator_with_context_manager] - assert '' == "I'm inner!\n"
FAILED test_public.py::test_all_cases[catching_IndexError] - AssertionError: assert '' == 'caught it!\n'
FAILED test_public.py::test_all_cases[catching_by_parent] - AssertionError: assert '' == 'caught it!\n'
FAILED test_public.py::test_all_cases[catching_all] - AssertionError: assert '' == 'caught it!\n'
FAILED test_public.py::test_all_cases[raise_and_catch_exception] - AssertionError: assert '' == 'Caught: oops\nAll done\n'
FAILED test_public.py::test_all_cases[raise_exception_from] - AssertionError: assert None == <class 'ValueError'>
FAILED test_public.py::test_all_cases[raise_and_catch_exception_in_function] - AssertionError: assert '' == 'Caught: oops\ndone\n'
FAILED test_public.py::test_all_cases[global_name_error] - AssertionError: assert <class 'KeyError'> == <class 'NameError'>
FAILED test_public.py::test_all_cases[global_name_error_in_try] - AssertionError: assert '' == 'No fooey\n'
FAILED test_public.py::test_all_cases[local_name_error] - AssertionError: assert <class 'IndexError'> == <class 'NameError'>
FAILED test_public.py::test_all_cases[catch_local_name_error] - AssertionError: assert '' == 'No fooey\n'
FAILED test_public.py::test_all_cases[reraise] - AssertionError: assert '' == 'No fooey\n'
FAILED test_public.py::test_all_cases[reraise_explicit_exception] - AssertionError: assert '' == 'Caught ouch\n'
FAILED test_public.py::test_all_cases[finally_while_throwing] - AssertionError: assert '' == 'About to..\nFinally\n'
FAILED test_public.py::test_all_cases[coverage_issue_92] - assert '' == "[0, 'f', 'e', 1, 'f', 'e', 2, 'f', 'e', 'r']\n"
FAILED test_public.py::test_all_cases[unpacking1] - AssertionError: assert '' == '[0, 1, 2] 3 4\n0 [1, 2, 3] 4\n0 1 [2, 3, 4]\n[] 0 1\n0 [] 1\n0 1 []\n'
FAILED test_public.py::test_all_cases[nested_loops] - AssertionError: assert '' == ('0 0 0\n'\n '0 0 1\n'\n '0 0 2\n'\n '0 0 3\n'\n '0 1 0\n'\n '0 1 1\n'\n '0 1 2\n'\n '0 1 3\n'\n '1 0 0\n'\n '1 0 1\n'\n '1 0 2\n'\n '1 0 3\n'...
FAILED test_public.py::test_all_cases[comprehensions] - AssertionError: assert '' == '[1, 2, 3, 4]\n'
FAILED test_public.py::test_all_cases[big_function] - assert '' == "-2\n-1\n10\n11\n12\n(13, 14)\n-3\n99\n-4\n[('z', -5), ('zz', -6)]\n"
FAILED test_public.py::test_all_cases[ackerman] - AssertionError: assert '' == '1 2 3 4 5\n2 3 4 5 6\n3 5 7 9 11\n5 13 29 61 125\n'
FAILED test_public.py::test_all_cases[small_closure] - AssertionError: assert '' == '100\n200\n'
FAILED test_public.py::test_all_cases[big_closure] - AssertionError: assert '' == 'foo\n1\nfoo\nfoo\n2\nfoo\nfoo\nfoo\nfoo\n4\n'
FAILED test_public.py::test_all_cases[binary_matrix_multiply] - AssertionError: assert '' == 'A(6)\n'
FAILED test_public.py::test_all_cases[inplace_matrix_multiply] - AssertionError: assert '' == 'A(6)\n'
FAILED test_public.py::test_all_cases[build_map_unpack_with_call] - assert '' == "[('a', 2), ('b', 3), ('c', 5)]\n"
FAILED test_public.py::test_all_cases[build_tuple_unpack_with_call] - AssertionError: assert '' == '(1, 2, 3, 4)\n'
FAILED test_public.py::test_all_cases[import_from] - AssertionError: assert '' == '2\n'
FAILED test_public.py::test_all_cases[import_name] - AssertionError: assert '' == '2\n'
FAILED test_public.py::test_all_cases[import_star] - AssertionError: assert '' == '2\n'
FAILED test_public.py::test_all_cases[store_attr] - AssertionError: assert '' == '3\n'
FAILED test_public.py::test_all_cases[delete_attr] - AssertionError: assert '' == 'None\n'
FAILED test_public.py::test_all_cases[get_awaitable] - AssertionError: assert <class 'AttributeError'> == <class 'ValueError'>
FAILED test_public.py::test_all_cases[get_awaitable_2] - assert '' == "[('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)]\n"
FAILED test_public.py::test_all_cases[get_awaitable_3] - assert '' == ('enter\n'\n 'enter\n'\n 'enter\n'\n 'exit\n'\n 'exit\n'\n 'exit\n'\n "[('enter', 'A', 2), ('enter', 'B', 3), ('enter', 'C', 4)]\n")
FAILED test_public.py::test_all_cases[setup_annotations] - assert '' == "[('a', typing.List[int]), ('b', <class 'str'>)]\n"
FAILED test_public.py::test_all_cases[load_global] - AssertionError: assert '' == '3\n'
FAILED test_public.py::test_all_cases[store_global] - AssertionError: assert '' == '5\n'
FAILED test_public.py::test_all_cases[delete_global] - AssertionError: assert '' == 'False\n'
FAILED test_public.py::test_all_cases[load_deref] - AssertionError: assert '' == '4\n'
FAILED test_public.py::test_all_cases[delete_deref] - AssertionError: assert '' == 'False\n'
FAILED test_public.py::test_all_cases[classderef] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[assignment_expression_if] - AssertionError: assert '' == 'List is too short (3 elements, expected >= 10)\n'
FAILED test_public.py::test_all_cases[self_explained_fstring] - assert 'Object: name=Eric, surname=Cartman is <non-printable speech here>\n' == "Object: name='Eric', surname='Cartman' is <non-printable speech here>\n"
FAILED test_public.py::test_all_cases[new_typings_setup_annotations] - assert '' == "[('a', list[int]), ('b', <class 'str'>)]\n"
FAILED test_public.py::test_all_cases[new_typings_features] - AssertionError: assert '' == 'True\n'
"""

s1 = """FAILED test_public.py::test_all_cases[simple] - AssertionError: assert '' == '17\n'
FAILED test_public.py::test_all_cases[globals] - AssertionError: assert '' == 'Pre: 2106\nMidst: 2107\nPost: 2107\n'
FAILED test_public.py::test_all_cases[building_list] - AssertionError: assert '' == '[2, 4, 6]\n'
FAILED test_public.py::test_all_cases[building_set] - AssertionError: assert '' == '{2, 4, 6}\n'
FAILED test_public.py::test_all_cases[generator_expression_in_join] - AssertionError: assert '' == 'Assert test case for generator_expression_in_join\n'
FAILED test_public.py::test_all_cases[generator_expression_complex] - AssertionError: assert '' == '    test_str\n'
FAILED test_public.py::test_all_cases[list_comprehension] - AssertionError: assert '' == 'Assert test case for list_comprehension\n'
FAILED test_public.py::test_all_cases[dict_comprehension] - AssertionError: assert '' == 'Assert test case for dict_comprehension\n'
FAILED test_public.py::test_all_cases[set_comprehension] - AssertionError: assert '' == 'Assert test case for set_comprehension\n'
FAILED test_public.py::test_all_cases[strange_sequence_ops] - AssertionError: assert '' == 'Assert test case for strange_sequence_ops\n'
FAILED test_public.py::test_all_cases[attributes] - AssertionError: assert '' == 'True 17\nFalse\n'
FAILED test_public.py::test_all_cases[attribute_inplace_ops] - AssertionError: assert '' == '14\n'
FAILED test_public.py::test_all_cases[deleting_names] - AssertionError: assert <class 'AttributeError'> == <class 'NameError'>
FAILED test_public.py::test_all_cases[deleting_local_names] - AssertionError: assert <class 'AttributeError'> == <class 'UnboundLocalError'>
FAILED test_public.py::test_all_cases[import] - AssertionError: assert '' == '3.141592653589793 2.718281828459045\n1.4142135623730951\n0.9092974268256817\n'
FAILED test_public.py::test_all_cases[classes] - AssertionError: assert '' == '2 3\n8 15\n'
FAILED test_public.py::test_all_cases[calling_methods_wrong] - AssertionError: assert <class 'AttributeError'> == <class 'TypeError'>
FAILED test_public.py::test_all_cases[calling_subclass_methods] - AssertionError: assert '' == '17\n'
FAILED test_public.py::test_all_cases[subclass_attribute] - AssertionError: assert '' == '17\n'
FAILED test_public.py::test_all_cases[subclass_attributes_not_shared] - AssertionError: assert '' == 'Assert test case for subclass_attributes_not_shared\n'
FAILED test_public.py::test_all_cases[data_descriptors_precede_instance_attributes] - AssertionError: assert '' == 'Assert test case for data_descriptors_precede_instance_attributes\n'
FAILED test_public.py::test_all_cases[instance_attrs_precede_non_data_descriptors] - AssertionError: assert '' == 'Assert test case for instance_attrs_precede_non_data_descriptors\n'
FAILED test_public.py::test_all_cases[subclass_attributes_dynamic] - AssertionError: assert '' == 'Assert test case for subclass_attributes_dynamic\n'
FAILED test_public.py::test_all_cases[attribute_access] - AssertionError: assert '' == '17\n17\n23\n'
FAILED test_public.py::test_all_cases[staticmethods] - AssertionError: assert '' == '1492\n1776\n'
FAILED test_public.py::test_all_cases[unbound_methods] - AssertionError: assert '' == '1815\n'
FAILED test_public.py::test_all_cases[bound_methods] - AssertionError: assert '' == '1815\n'
FAILED test_public.py::test_all_cases[callback] - assert '' == "['ABC', 'xyz']\nAssert test case for callback\n"
FAILED test_public.py::test_all_cases[jump_if_true_or_pop] - AssertionError: assert '' == 'Assert test case for jump_if_true_or_pop\n'
FAILED test_public.py::test_all_cases[jump_if_false_or_pop] - AssertionError: assert '' == 'Assert test case for jump_if_false_or_pop\n'
FAILED test_public.py::test_all_cases[pop_jump_if_true0] - AssertionError: assert '' == 'Assert test case for pop_jump_if_true\n'
FAILED test_public.py::test_all_cases[decorator] - AssertionError: assert '' == 'Test case decorator\n'
FAILED test_public.py::test_all_cases[multiple_classes] - AssertionError: assert '' == '6\n7\n'
FAILED test_public.py::test_all_cases[continue_in_try_except] - AssertionError: assert '' == '1\n2\n4\n5\n7\n8\ndone\n'
FAILED test_public.py::test_all_cases[continue_in_try_finally] - AssertionError: assert '' == '.\n1\n.\n2\n.\n.\n4\n.\n5\n.\n.\n7\n.\n8\n.\n.\ndone\n'
FAILED test_public.py::test_all_cases[in] - AssertionError: assert '' == 'Assert test case for in\n'
FAILED test_public.py::test_all_cases[is] - AssertionError: assert '' == 'Assert test case for is\n'
FAILED test_public.py::test_all_cases[functions] - assert '' == ('1 17 Hello [99]\n'\n '2 3 Hello [99, 99]\n'\n '3 17 Bye [99, 99, 99]\n'\n "4 17 Hello ['What?', 99]\n"\n '5 b c [99, 99, 99, 99]\n')
FAILED test_public.py::test_all_cases[recursion] - AssertionError: assert '' == '720\nAssert test case for recursion\n'
FAILED test_public.py::test_all_cases[nested_names] - AssertionError: assert '' == '2\n1\n'
FAILED test_public.py::test_all_cases[calling_functions_with_args_kwargs] - AssertionError: assert '' == '6 77 88 [99]\n7 17 23 [99, 99]\n6 77 23 [123, 99]\n'
FAILED test_public.py::test_all_cases[defining_functions_with_args] - AssertionError: assert '' == 'args is (1, 2)\n'
FAILED test_public.py::test_all_cases[defining_functions_with_kwargs] - assert '' == "kwargs is [('blue', False), ('red', True)]\n"
FAILED test_public.py::test_all_cases[defining_functions_with_args_kwargs] - assert '' == "args is (1, 2)\nkwargs is [('blue', False), ('red', True)]\n"
FAILED test_public.py::test_all_cases[defining_functions_with_positional_args_kwargs] - assert '' == ("x is 'a', y is 'b'\n"\n 'args is (1, 2)\n'\n "kwargs is [('blue', False), ('red', True)]\n")
FAILED test_public.py::test_all_cases[defining_functions_with_keyword_only] - AssertionError: assert '' == 'x is 1, y is 2\n'
FAILED test_public.py::test_all_cases[defining_functions_with_positional_only_ordinary_and_keyword_only] - AssertionError: assert <class 'AttributeError'> == <class 'TypeError'>
FAILED test_public.py::test_all_cases[defining_functions_with_empty_args] - AssertionError: assert '' == 'args is ()\n'
FAILED test_public.py::test_all_cases[defining_functions_with_empty_kwargs] - AssertionError: assert '' == 'kwargs is []\n'
FAILED test_public.py::test_all_cases[defining_functions_with_empty_args_kwargs] - AssertionError: assert '' == 'args is (), kwargs is {}\n'
FAILED test_public.py::test_all_cases[partial] - AssertionError: assert '' == 'Assert test case for partial\n'
FAILED test_public.py::test_all_cases[partial_with_kwargs] - AssertionError: assert '' == 'Assert test case for partial_with_kwargs\n'
FAILED test_public.py::test_all_cases[wraps] - AssertionError: assert '' == 'Calling decorated function\nAssert test case for wraps\n'
FAILED test_public.py::test_all_cases[closures] - AssertionError: assert '' == '17\nAssert test case for closures\n'
FAILED test_public.py::test_all_cases[closures_store_deref] - AssertionError: assert '' == '28\nAssert test case for closures_store_deref\n'
FAILED test_public.py::test_all_cases[closures_in_loop] - AssertionError: assert '' == '0\n1\n2\nAssert test case for closures_in_loop\n'
FAILED test_public.py::test_all_cases[closures_with_defaults] - AssertionError: assert '' == '88\nAssert test case for closures_with_defaults\n'
FAILED test_public.py::test_all_cases[deep_closures] - AssertionError: assert '' == '54\nAssert test case for deep_closures\n'
FAILED test_public.py::test_all_cases[first] - AssertionError: assert '' == '1\n2\n'
FAILED test_public.py::test_all_cases[partial_generator] - AssertionError: assert '' == 'Assert test case for partial_generator\n'
FAILED test_public.py::test_all_cases[yield_multiple_values] - AssertionError: assert '' == '1 2 3\n4 5 6\n'
FAILED test_public.py::test_all_cases[simple_generator] - AssertionError: assert '' == '[0, 1, 2]\n'
FAILED test_public.py::test_all_cases[generator_from_generator] - AssertionError: assert '' == '[1, 2, 5, 10, 17]\n'
FAILED test_public.py::test_all_cases[generator_from_generator2] - assert '' == "[('abc', 'ABC'), ('def', 'DEF')]\n"
FAILED test_public.py::test_all_cases[yield_from] - AssertionError: assert '' == 'Hello, World\n'
FAILED test_public.py::test_all_cases[yield_from_tuple] - AssertionError: assert '' == '1\n2\n3\n4\n'
FAILED test_public.py::test_all_cases[generator] - AssertionError: assert '' == 'Test case generator\n'
FAILED test_public.py::test_all_cases[distinguish_iterators_and_generators] - AssertionError: assert '' == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'
FAILED test_public.py::test_all_cases[nested_yield_from] - AssertionError: assert '' == 'Hello, World\n'
FAILED test_public.py::test_all_cases[return_from_generator] - AssertionError: assert '' == '1\n2\n'
FAILED test_public.py::test_all_cases[return_from_generator_with_yield_from] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[test2] - AssertionError: assert '' == '100\n'
FAILED test_public.py::test_all_cases[test5] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test6] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test11] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test12] - AssertionError: assert '' == '7\n'
FAILED test_public.py::test_all_cases[test13] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test24] - AssertionError: assert '' == 'False\n'
FAILED test_public.py::test_all_cases[test26] - AssertionError: assert '' == '4Me\n'
FAILED test_public.py::test_all_cases[test27] - AssertionError: assert '' == '2\n'
FAILED test_public.py::test_all_cases[test34] - AssertionError: assert '' == '3\n'
FAILED test_public.py::test_all_cases[test35] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[test36] - AssertionError: assert '' == '8\n'
FAILED test_public.py::test_all_cases[test38] - AssertionError: assert '' == '5\n'
FAILED test_public.py::test_all_cases[test43] - AssertionError: assert '' == '7\n'
FAILED test_public.py::test_all_cases[test46] - AssertionError: assert '' == '10\n'
FAILED test_public.py::test_all_cases[test47] - AssertionError: assert '' == '100\n'
FAILED test_public.py::test_all_cases[test49] - AssertionError: assert '' == '100\n'
FAILED test_public.py::test_all_cases[test50] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[test51] - AssertionError: assert '' == '100\n'
FAILED test_public.py::test_all_cases[test52] - AssertionError: assert '' == '10000\n'
FAILED test_public.py::test_all_cases[test53] - AssertionError: assert '' == '6\n'
FAILED test_public.py::test_all_cases[test54] - AssertionError: assert '' == '5\n'
FAILED test_public.py::test_all_cases[test55] - AssertionError: assert '' == '1\n2\n3\n'
FAILED test_public.py::test_all_cases[test56] - AssertionError: assert '' == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n'
FAILED test_public.py::test_all_cases[test57] - AssertionError: assert '' == '[1, 3, 5, 7, 9]\n'
FAILED test_public.py::test_all_cases[test58] - AssertionError: assert '' == '[1, 9, 25, 49, 81]\n'
FAILED test_public.py::test_all_cases[test60] - AssertionError: assert '' == '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
FAILED test_public.py::test_all_cases[test61] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[test62] - AssertionError: assert '' == '30\n'
FAILED test_public.py::test_all_cases[test63] - AssertionError: assert '' == '110\n'
FAILED test_public.py::test_all_cases[test64] - AssertionError: assert '' == '100010\n'
FAILED test_public.py::test_all_cases[test71] - AssertionError: assert '' == '3\n'
FAILED test_public.py::test_all_cases[test72] - AssertionError: assert '' == '2 1\n'
FAILED test_public.py::test_all_cases[test75] - AssertionError: assert '' == '2\n3\n4\n'
FAILED test_public.py::test_all_cases[test76] - AssertionError: assert '' == '1\n2\n3\n'
FAILED test_public.py::test_all_cases[test78] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test79] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test89] - AssertionError: assert '' == '1\n(2, 3, 4, 5, 6)\n'
FAILED test_public.py::test_all_cases[test90] - AssertionError: assert '' == '(1, 3, 5)\n(2, 4, 6)\n'
FAILED test_public.py::test_all_cases[test91] - AssertionError: assert '' == '(2, 3)\n(3, 4, 5)\n'
FAILED test_public.py::test_all_cases[test98] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test99] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test100] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[test101] - AssertionError: assert '' == 'True\n'
FAILED test_public.py::test_all_cases[simple_context_manager] - assert '' == "Look: 'iwoeiwoeiwoer'\n"
FAILED test_public.py::test_all_cases[raise_in_context_manager] - assert '' == "Look: 'iwoxr'\n"
FAILED test_public.py::test_all_cases[suppressed_raise_in_context_manager] - assert '' == "Look: 'iwoer'\n"
FAILED test_public.py::test_all_cases[return_in_with] - assert '' == "Look: 'iwor'\n"
FAILED test_public.py::test_all_cases[continue_in_with] - assert '' == "Look: 'iwzoeiwoiwzoer'\n"
FAILED test_public.py::test_all_cases[break_in_with] - assert '' == "Look: 'iwzoeiwor'\n"
FAILED test_public.py::test_all_cases[raise_in_with] - assert '' == "Look: 'iwoxr'\n"
FAILED test_public.py::test_all_cases[at_context_manager_simplified] - AssertionError: assert '' == 'Assert test case for at_context_manager_simplified\n'
FAILED test_public.py::test_all_cases[at_context_manager_complete] - AssertionError: assert '' == 'Assert test case for at_context_manager_complete\n'
FAILED test_public.py::test_all_cases[generator_with_context_manager] - assert '' == "I'm inner!\n"
FAILED test_public.py::test_all_cases[catching_IndexError] - AssertionError: assert '' == 'caught it!\n'
FAILED test_public.py::test_all_cases[catching_by_parent] - AssertionError: assert '' == 'caught it!\n'
FAILED test_public.py::test_all_cases[catching_all] - AssertionError: assert '' == 'caught it!\n'
FAILED test_public.py::test_all_cases[raise_exception] - AssertionError: assert <class 'AttributeError'> == <class 'ValueError'>
FAILED test_public.py::test_all_cases[raise_exception_class] - AssertionError: assert <class 'AttributeError'> == <class 'ValueError'>
FAILED test_public.py::test_all_cases[raise_and_catch_exception] - AssertionError: assert '' == 'Caught: oops\nAll done\n'
FAILED test_public.py::test_all_cases[raise_exception_from] - AssertionError: assert <class 'AttributeError'> == <class 'ValueError'>
FAILED test_public.py::test_all_cases[raise_and_catch_exception_in_function] - AssertionError: assert '' == 'Caught: oops\ndone\n'
FAILED test_public.py::test_all_cases[global_name_error] - AssertionError: assert <class 'KeyError'> == <class 'NameError'>
FAILED test_public.py::test_all_cases[global_name_error_in_try] - AssertionError: assert '' == 'No fooey\n'
FAILED test_public.py::test_all_cases[local_name_error] - AssertionError: assert <class 'AttributeError'> == <class 'NameError'>
FAILED test_public.py::test_all_cases[catch_local_name_error] - AssertionError: assert '' == 'No fooey\n'
FAILED test_public.py::test_all_cases[reraise] - AssertionError: assert '' == 'No fooey\n'
FAILED test_public.py::test_all_cases[reraise_explicit_exception] - AssertionError: assert '' == 'Caught ouch\n'
FAILED test_public.py::test_all_cases[finally_while_throwing] - AssertionError: assert '' == 'About to..\nFinally\n'
FAILED test_public.py::test_all_cases[coverage_issue_92] - assert '' == "[0, 'f', 'e', 1, 'f', 'e', 2, 'f', 'e', 'r']\n"
FAILED test_public.py::test_all_cases[unpacking1] - AssertionError: assert '' == '[0, 1, 2] 3 4\n0 [1, 2, 3] 4\n0 1 [2, 3, 4]\n[] 0 1\n0 [] 1\n0 1 []\n'
FAILED test_public.py::test_all_cases[comprehensions] - AssertionError: assert '' == '[1, 2, 3, 4]\n'
FAILED test_public.py::test_all_cases[simple_function] - AssertionError: assert '' == '[1]\n[1, 1]\n'
FAILED test_public.py::test_all_cases[big_function] - assert '' == "-2\n-1\n10\n11\n12\n(13, 14)\n-3\n99\n-4\n[('z', -5), ('zz', -6)]\n"
FAILED test_public.py::test_all_cases[ackerman] - AssertionError: assert '' == '1 2 3 4 5\n2 3 4 5 6\n3 5 7 9 11\n5 13 29 61 125\n'
FAILED test_public.py::test_all_cases[small_closure] - AssertionError: assert '' == '100\n200\n'
FAILED test_public.py::test_all_cases[big_closure] - AssertionError: assert '' == 'foo\n1\nfoo\nfoo\n2\nfoo\nfoo\nfoo\nfoo\n4\n'
FAILED test_public.py::test_all_cases[make_function] - AssertionError: assert '' == 'Make function test case\n'
FAILED test_public.py::test_all_cases[binary_matrix_multiply] - AssertionError: assert '' == 'A(6)\n'
FAILED test_public.py::test_all_cases[inplace_matrix_multiply] - AssertionError: assert '' == 'A(6)\n'
FAILED test_public.py::test_all_cases[build_list] - AssertionError: assert '' == '[1, 2, 3]\n[1, 2, 3]\n'
FAILED test_public.py::test_all_cases[build_list_unpack] - AssertionError: assert '' == '[1, 2, 3, 4]\n'
FAILED test_public.py::test_all_cases[build_map_unpack] - AssertionError: assert '' == '[(1, 2), (2, 4), (3, 5)]\n'
FAILED test_public.py::test_all_cases[build_map_unpack_with_call] - assert '' == "[('a', 2), ('b', 3), ('c', 5)]\n"
FAILED test_public.py::test_all_cases[build_set] - AssertionError: assert '' == '[1, 2]\n[1, 2]\n'
FAILED test_public.py::test_all_cases[build_set_unpack] - AssertionError: assert '' == '[1, 2]\n'
FAILED test_public.py::test_all_cases[build_slice] - AssertionError: assert '' == '[2, 3, 4]\n'
FAILED test_public.py::test_all_cases[build_tuple_unpack] - AssertionError: assert '' == '(1, 2, 3, 4)\n'
FAILED test_public.py::test_all_cases[build_tuple_unpack_with_call] - AssertionError: assert '' == '(1, 2, 3, 4)\n'
FAILED test_public.py::test_all_cases[import_from] - AssertionError: assert '' == '2\n'
FAILED test_public.py::test_all_cases[import_name] - AssertionError: assert '' == '2\n'
FAILED test_public.py::test_all_cases[import_star] - AssertionError: assert '' == '2\n'
FAILED test_public.py::test_all_cases[load_attr] - AssertionError: assert '' == '3\n'
FAILED test_public.py::test_all_cases[store_attr] - AssertionError: assert '' == '3\n'
FAILED test_public.py::test_all_cases[delete_attr] - AssertionError: assert '' == 'None\n'
FAILED test_public.py::test_all_cases[load_fast] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[store_fast] - AssertionError: assert '' == 'None\n'
FAILED test_public.py::test_all_cases[delete_fast] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[get_awaitable] - AssertionError: assert <class 'AttributeError'> == <class 'ValueError'>
FAILED test_public.py::test_all_cases[get_awaitable_2] - assert '' == "[('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)]\n"
FAILED test_public.py::test_all_cases[get_awaitable_3] - assert '' == ('enter\n'\n 'enter\n'\n 'enter\n'\n 'exit\n'\n 'exit\n'\n 'exit\n'\n "[('enter', 'A', 2), ('enter', 'B', 3), ('enter', 'C', 4)]\n")
FAILED test_public.py::test_all_cases[setup_annotations] - assert '' == "[('a', typing.List[int]), ('b', <class 'str'>)]\n"
FAILED test_public.py::test_all_cases[load_global] - AssertionError: assert '' == '3\n'
FAILED test_public.py::test_all_cases[store_global] - AssertionError: assert '' == '5\n'
FAILED test_public.py::test_all_cases[delete_global] - AssertionError: assert '' == 'False\n'
FAILED test_public.py::test_all_cases[load_deref] - AssertionError: assert '' == '4\n'
FAILED test_public.py::test_all_cases[delete_deref] - AssertionError: assert '' == 'False\n'
FAILED test_public.py::test_all_cases[classderef] - AssertionError: assert '' == '1\n'
FAILED test_public.py::test_all_cases[assignment_expression_if] - AssertionError: assert '' == 'List is too short (3 elements, expected >= 10)\n'
FAILED test_public.py::test_all_cases[assignment_expression_while] - AssertionError: assert '' == '1\n2\n3\n'
FAILED test_public.py::test_all_cases[self_explained_fstring] - assert 'Object: name=Eric, surname=Cartman is <non-printable speech here>\n' == "Object: name='Eric', surname='Cartman' is <non-printable speech here>\n"
FAILED test_public.py::test_all_cases[set_union] - AssertionError: assert '' == '[1, 2]\n'
FAILED test_public.py::test_all_cases[new_typings_setup_annotations] - assert '' == "[('a', list[int]), ('b', <class 'str'>)]\n"
FAILED test_public.py::test_all_cases[new_typings_features] - AssertionError: assert '' == 'True\n'
"""

result = set(s.split('\n')) - set(s1.split('\n'))
for i in result:
    print(i)
print(len(result))