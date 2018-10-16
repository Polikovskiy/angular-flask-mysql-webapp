import {TemplateRef, ViewChild} from '@angular/core';
import {Component, OnInit} from '@angular/core';
import {User} from './user';
import {UserService} from './user.service';
import {Observable} from 'rxjs';
import {Transfer_log} from './transfer_log';
import {Ubsusers} from './ubsusers';
import {GenerateDateService} from './generate_date.service'


@Component({ 
    selector: 'generateDate', 
    templateUrl: './generate_data.component.html',
    providers: [GenerateDateService]
}) 
export class GenerateDataComponent implements OnInit {
    //типы шаблонов
    @ViewChild('readOnlyTemplate') readOnlyTemplate: TemplateRef<any>;
    @ViewChild('editTemplate') editTemplate: TemplateRef<any>;
      
    transfer_logs: Array<Transfer_log>;
    ubsusers: Array<Ubsusers>;
    statusMessage:string
    month:number
      
    constructor(private serv: GenerateDateService) {
        this.ubsusers = new Array<Ubsusers>();
        this.transfer_logs = new Array<Transfer_log>();
    }
      
    ngOnInit() {
        this.month = 6;
    }
      
    //загрузка ланных с сервера
    show(month:number) {
        this.serv.show(this.month).subscribe((data: Ubsusers[]) => {
                this.ubsusers = data;
            });

    }

    // сгенерировать данные на сервере
    generate_data() {
        this.serv.generate_data().subscribe(data => {

                if (data == "ok") {
                    this.statusMessage = 'Data generated'
                } else {
                    this.statusMessage = 'Data failure'
                }

            });
    }

    loadTemplate() {
            return this.readOnlyTemplate;
    }
}