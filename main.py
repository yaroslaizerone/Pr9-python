from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse

# создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()


# определяем зависимость
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# получаем разметку
@app.get("/")
def main():
    return FileResponse("public/index.html")


#получаем данные о студентах
@app.get("/api/student")
def get_people(db: Session = Depends(get_db)):
    return db.query(Student).all()


#получаем данные о группах
@app.get("/api/group")
def get_people(db: Session = Depends(get_db)):
    return db.query(Group).all()


@app.get("/api/student/{id_student}")
def get_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Student).filter(Student.id_student == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Студент не найден"})
    # если пользователь найден, отправляем его
    


@app.get("/api/group/{id_group}")
def get_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    group = db.query(Group).filter(Group.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if group == None:
        return JSONResponse(status_code=404, content={"message": "Группа не найдена"})
    # если пользователь найден, отправляем его
    return group


#Создание студента
@app.post("/api/student")
def create_person(data=Body(), db: Session = Depends(get_db)):
    person = Student(id_group=data["id_group"]
                     , first_name=data["first_name"], last_name=data["last_name"],
                     age=data["age"], birth_date=data["birth_date"], login=data["login"], password=data["password"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


#Создание Группы
@app.post("/api/student")
def create_person(data=Body(), db: Session = Depends(get_db)):
    group = Group(id_group=data["id_group"], name_group=data["name_group"])
    db.add(group)
    db.commit()
    db.refresh(group)
    return group


#Изменение Студента
@app.put("/api/student")
def edit_person(data=Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Student).filter(Student.id_student == data["id_student"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Студент не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.id_student = data["Номер студента"]
    person.id_group = data["Номер Группы"]
    person.first_name = data["Имя"]
    person.last_name = data["Фамилия"]
    person.age = data["Возраст"]
    person.birth_date = data["День рождения"]
    person.login = data["Логин"]
    person.password = data["Пароль"]
    db.commit()  # сохраняем изменения
    db.refresh(person)
    return person

#Изменение Группы
@app.put("/api/student")
def edit_person(data=Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    group = db.query(Group).filter(Group.id_group == data["id_group"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if group == None:
        return JSONResponse(status_code=404, content={"message": "Группа не найдена"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    group.id_group = data["Номер группы"]
    group.name = data["Название группы"]
    db.commit()  # сохраняем изменения
    db.refresh(group)
    return group


#Удаление Студента
@app.delete("/api/student/{id_student}")
def delete_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Student).filter(Student.id == id).first()

    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Студент не найден"})

    # если пользователь найден, удаляем его
    db.delete(person)  # удаляем объект
    db.commit()  # сохраняем изменения
    return person


#Удаление Группы
@app.delete("/api/student/{id_student}")
def delete_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    group = db.query(Group).filter(Group.id == id).first()

    # если не найден, отправляем статусный код и сообщение об ошибке
    if group == None:
        return JSONResponse(status_code=404, content={"message": "Группа не найдена"})

    # если группа найден, удаляем его
    db.delete(group)  # удаляем объект
    db.commit()  # сохраняем изменения
    return group