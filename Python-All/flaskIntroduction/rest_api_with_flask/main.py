# -*- coding: UTF-8 -*-

"""W tym projekcie używam modułu json do otwieranai i operowania na plikach json"""
import json

from typing import Optional
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    """
    Moja podstawowa klasa, która będzie tworzyć obiekty do pliku json.
    """

    id: Optional[int] = None
    first_name: str
    last_name: str
    gender: str
    age: int


with open("people.json", "r+", encoding="utf-8") as file_json:
    people = json.load(file_json)


@app.get("/person/{person_id}", status_code=200)
def get_person(person_id: int):
    """
    Funkcja zwracająca obiekt na stronie Internetowej.
    """
    person = [p for p in people if p["id"] == person_id]
    return person[0] if len(person) > 0 else {}


@app.get("/search", status_code=200)
def search_person(
    age: Optional[int] = Query(None, title="age", description="Wiek do filtrowania."),
    first_name: Optional[str] = Query(
        None, title="first_name", description="Imię do filtrowania."
    ),
):
    """
    Funkcja szukająca obiektu w bazie danych.
    """
    people1 = [p for p in people if p["age"] == age]

    if first_name is None:
        if age is None:
            return people
        else:
            return people1
    else:
        people2 = [p for p in people if first_name.lower() in p["first_name"].lower()]
        if age is None:
            return people2
        else:
            combined = [p for p in people1 if p in people2]
            return combined


@app.post("/addPerson", status_code=201)
def add_person(person: Person):
    """
    Funkcja dodająca obiekt do pliku json.
    """
    p_id = max([p["id"] for p in people]) + 1 if len(people) > 0 else 1
    new_person = {
        "id": p_id,
        "first_name": person.first_name,
        "last_name": person.last_name,
        "gender": person.gender,
        "age": person.age,
    }
    people.append(new_person)
    with open("people.json", "w", encoding="utf-8") as f:
        json.dump(people, f)
    return new_person


@app.put("/updatePerson", status_code=204)
def update_person(person: Person):
    """
    Funkcja aktualizująca obiekt w pliku json.
    """
    new_person = {
        "id": person.id,
        "first_name": person.first_name,
        "last_name": person.last_name,
        "gender": person.gender,
        "age": person.age,
    }
    person_list = [p for p in people if p["id"] == person.id]
    if len(person_list) > 0:
        people.remove(person_list[0])
        people.append(new_person)
        with open("people.json", "w", encoding="utf-8") as file_json_in_update:
            json.dump(people, file_json_in_update)
        return new_person
    else:
        return HTTPException(
            status_code=404, detail=f"Osoba z id: {person.id} nie znaleziona!"
        )


@app.delete("/deletePerson/{person_id}", status_code=204)
def delete_person(person_id: int):
    """
    Funkcja usuwająca obiekt z pliku json.
    """
    person_list = [p for p in people if p["id"] == person_id]
    if len(person_list) > 0:
        people.remove(person_list[0])
        with open("people.json", "w", encoding="utf-8") as f:
            json.dump(people, f)
        return person_list[0]
    else:
        return HTTPException(
            status_code=404, detail=f"Osoba z id: {person_id} nie znaleziona!"
        )
