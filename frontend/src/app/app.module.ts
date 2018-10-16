import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpClientModule }   from '@angular/common/http';
import { AppComponent }   from './app.component';
import { CompanyComponent }   from './company.component';
import { GenerateDataComponent }   from './generate_data.component';

@NgModule({
    imports:      [ BrowserModule, FormsModule, HttpClientModule],
    declarations: [ AppComponent, CompanyComponent, GenerateDataComponent],
    bootstrap:    [ AppComponent, CompanyComponent, GenerateDataComponent]
})
export class AppModule { }
