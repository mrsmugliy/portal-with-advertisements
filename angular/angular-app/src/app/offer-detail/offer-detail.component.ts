import {Component, OnInit} from '@angular/core';
import {ApiService} from '../api.service';
import {ActivatedRoute, Router} from '@angular/router';
import {Location, LocationStrategy, PathLocationStrategy} from '@angular/common';

@Component({
  selector: 'app-offer-detail',
  templateUrl: './offer-detail.component.html',
  styleUrls: ['./offer-detail.component.sass'],
  providers: [Location, {provide: LocationStrategy, useClass: PathLocationStrategy}]
})
export class OfferDetailComponent implements OnInit {

  offer: any;

  constructor(private api: ApiService,
              private rout: ActivatedRoute,
              private location: Location) {
    this.getOffer();
  }

  id = this.rout.snapshot.paramMap.get('id');
  getOffer = () => {
    this.api.getOneOffer(this.id).subscribe(
      data => {
        this.offer = data;
        console.log(this.offer);
      },
      error => {
        console.log(error);
      }
    );
  }

  // tslint:disable-next-line:typedef
  goBack() {
    this.location.back();
  }
  ngOnInit(): void {
  }

}
