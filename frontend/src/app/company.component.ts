import {TemplateRef, ViewChild} from '@angular/core';
import {Component, OnInit} from '@angular/core';
import {Company} from './company';
import {CompanyService} from './company.service';
import {Observable} from 'rxjs';
  
@Component({ 
    selector: 'company', 
    templateUrl: './company.component.html',
    providers: [CompanyService]
}) 
export class CompanyComponent implements OnInit {
    //типы шаблонов
    @ViewChild('readOnlyTemplate') readOnlyTemplate: TemplateRef<any>;
    @ViewChild('editTemplate') editTemplate: TemplateRef<any>;
      
    editedCompany: Company;
    companys: Array<Company>;
    isNewRecord: boolean;
    statusMessage: string;
      
    constructor(private serv: CompanyService) {
        this.companys = new Array<Company>();
    }
      
    ngOnInit() {
        this.loadCompanys();
    }
      
    //загрузка компаний
    private loadCompanys() {
        this.serv.getCompanys().subscribe((data: Company[]) => {
                this.companys = data;  
            });
    }
    // добавление компании
    addCompany() {
        this.editedCompany = new Company(0,"",0);
        this.companys.push(this.editedCompany);
        this.isNewRecord = true;
    }
   
    // редактирование компании
    editCompany(company: Company) {
        this.editedCompany = new Company(company.Id, company.Name, company.Quota);
    }
    // загружаем один из двух шаблонов
    loadTemplate(company: Company) {
        if (this.editedCompany && this.editedCompany.Id == company.Id) {
            return this.editTemplate;
        } else {
            return this.readOnlyTemplate;
        }
    }
    // сохраняем компанию
    saveCompany() {
        if (this.isNewRecord) {
            // добавляем компанию
            console.log(this.editedCompany)
            this.serv.createCompany(this.editedCompany).subscribe(data => {
                this.statusMessage = 'company added',
                this.loadCompanys();
            });
            this.isNewRecord = false;
            this.editedCompany = null;
        } else {
            // изменяем компанию
            this.serv.updateCompany(this.editedCompany.Id, this.editedCompany).subscribe(data => {
                this.statusMessage = 'company updated',
                this.loadCompanys();
            });
            this.editedCompany = null;
        }
    }
    // отмена редактирования
    cancel() {
        // если отмена при добавлении, удаляем последнюю запись
        if (this.isNewRecord) {
            this.companys.pop();
            this.isNewRecord = false;
        }
        this.editedCompany = null;
    }
    // удаление компании
    deleteCompany(company: Company) {
        this.serv.deleteCompany(company.Id).subscribe(data => {
            this.statusMessage = 'company delete',
            this.loadCompanys();
        });
    }
}