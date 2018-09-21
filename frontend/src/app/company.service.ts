import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {Company} from './company';
import {Observable} from 'rxjs';
   
@Injectable()
export class CompanyService{
   
    private url = "http://localhost:5000/company";
    constructor(private http: HttpClient){ }
      
    getCompanys(){
        return this.http.get(this.url);
    }
  
    createCompany(company: Company){
        return this.http.post(this.url, company); 
    }
    updateCompany(id: number, company: Company) {
        const urlParams = new HttpParams().set("id", id.toString());
        return this.http.put(this.url, company, { params: urlParams});
    }
    deleteCompany(id: number){
        const urlParams = new HttpParams().set("id", id.toString());
        return this.http.delete(this.url, { params: urlParams});
    }
}
