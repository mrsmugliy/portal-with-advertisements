import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrls = 'http://127.0.0.1:8000/api/';
  httpHeaders = new HttpHeaders({'Content-type': 'application/json'});

  constructor(private http: HttpClient) { }

  getAllOffer(): Observable<any>{
    return this.http.get(this.baseUrls + 'offers/',
      {headers: this.httpHeaders});
  }
  getOneOffer(id): Observable<any>{
    return this.http.get(this.baseUrls + 'offers/' + id,
      {headers: this.httpHeaders});
  }
}
