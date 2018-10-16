import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {User} from './user';
import {Observable} from 'rxjs';
import {Transfer_log} from './transfer_log';
import {Ubsusers} from './ubsusers';
   
@Injectable()
export class GenerateDateService{
   
    private url = "http://localhost:5000/generate_data";
    private url_show = "http://localhost:5000/show";
    constructor(private http: HttpClient){ }
    
    show(month: number){
        const urlParams = new HttpParams().set("month", month.toString());
        return this.http.post(this.url_show, month);
    }

    generate_data(){
        return this.http.get(this.url);
    }

    
}