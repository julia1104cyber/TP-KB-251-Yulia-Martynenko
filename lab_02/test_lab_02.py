import pytest
from lab_02 import add_student, delete_student, update_student

def test_add_student():
    test_list = []
    add_student(test_list, "Zak", "111", "20", "z@test.com")
    add_student(test_list, "Bob", "222", "19", "b@test.com")
    
    assert len(test_list) == 2
    assert test_list[0]["name"] == "Bob"
    assert test_list[1]["name"] == "Zak"

def test_delete_student():
    test_list = [{"name": "Bob", "phone": "222", "age": "19", "email": "b@test.com"}]
    
    assert delete_student(test_list, "Bob") == True
    assert len(test_list) == 0
    
    assert delete_student(test_list, "Alice") == False

def test_update_student():
    test_list = [{"name": "Bob", "phone": "222", "age": "19", "email": "b@test.com"}]
    
    result = update_student(test_list, "Bob", "Alice", "333", "20", "a@test.com")
    assert result == True
    assert test_list[0]["name"] == "Alice"
    assert test_list[0]["phone"] == "333"