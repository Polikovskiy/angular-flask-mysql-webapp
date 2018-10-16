import {TemplateRef, ViewChild} from '@angular/core';
import {Component, OnInit} from '@angular/core';
import {User} from './user';
import {UserService} from './user.service';
import {Observable} from 'rxjs';
  
@Component({ 
    selector: 'my-app', 
    templateUrl: './app.component.html',
    providers: [UserService]
}) 
export class AppComponent implements OnInit {
    //типы шаблонов
    @ViewChild('readOnlyTemplate') readOnlyTemplate: TemplateRef<any>;
    @ViewChild('editTemplate') editTemplate: TemplateRef<any>;
      
    editedUser: User;
    users: Array<User>;
    isNewRecord: boolean;
    statusMessage: string;
      
    constructor(private serv: UserService) {
        this.users = new Array<User>();
    }
      
    ngOnInit() {
        this.loadUsers();
    }
      
    //загрузка пользователей
    private loadUsers() {
        this.serv.getUsers().subscribe((data: User[]) => {
                this.users = data;  
            });
    }
    // добавление пользователя
    addUser() {
        this.editedUser = new User(0,"e","e",0);
        this.users.push(this.editedUser);
        this.isNewRecord = true;
        console.log(this.isNewRecord)
    }
   
    // редактирование пользователя
    editUser(user: User) {
        this.editedUser = new User(user.Id, user.Name, user.Email, user.Company);
    }
    // загружаем один из двух шаблонов
    loadTemplate(user: User) {
        if (this.editedUser && this.editedUser.Id == user.Id) {
            return this.editTemplate;
        } else {
            return this.readOnlyTemplate;
        }
    }
    // сохраняем пользователя
    saveUser() {
        if (this.isNewRecord) {
            // добавляем пользователя
            console.log(this.editedUser)
            this.serv.createUser(this.editedUser).subscribe(data => {
                if (data == "ok") {
                    this.statusMessage = 'user added',
                    this.loadUsers();
                } else {
                    this.statusMessage = 'add failure',
                    this.loadUsers();
                }

            });
            this.isNewRecord = false;
            this.editedUser = null;
        } else {
            // изменяем пользователя
            console.log(this.editedUser+"create")
            this.serv.updateUser(this.editedUser.Id, this.editedUser).subscribe(data => {
                this.statusMessage = 'Users updated',
                this.loadUsers();
            });
            this.editedUser = null;
        }
    }
    // отмена редактирования
    cancel() {
        // если отмена при добавлении, удаляем последнюю запись
        if (this.isNewRecord) {
            this.users.pop();
            this.isNewRecord = false;
        }
        this.editedUser = null;
    }
    // удаление пользователя
    deleteUser(user: User) {
        this.serv.deleteUser(user.Id).subscribe(data => {
            this.statusMessage = 'users delete',
            this.loadUsers();
        });
    }
}