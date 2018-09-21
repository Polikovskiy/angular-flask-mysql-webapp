import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpClientModule }   from '@angular/common/http';
import { AppComponent }   from './app.component';
import { CompanyComponent }   from './company.component';
@NgModule({
    imports:      [ BrowserModule, FormsModule, HttpClientModule],
    declarations: [ AppComponent, CompanyComponent ],
    bootstrap:    [ AppComponent, CompanyComponent ]
})
export class AppModule { }
