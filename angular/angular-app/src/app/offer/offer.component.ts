import {Component, OnInit} from '@angular/core';
import {ApiService} from '../api.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-offer',
  templateUrl: './offer.component.html',
  styleUrls: ['./offer.component.sass']
})
export class OfferComponent implements OnInit {

  offers: any;
  category: string;

  constructor(private api: ApiService,
              private route: Router) {

  }

  getOffer = () => {
    this.api.getAllOffer().subscribe(
      data => {
        this.offers = data;
      },
      error => {
        console.log(error);
      }
    );
  }
  selectOffer = (offer) => {
    this.route.navigate(['offers', offer.id]);
  }

  ngOnInit(): void {
    this.getOffer();
  }
  Search = () => {
    if (this.category) {
      this.offers = this.offers.filter(res => {
        return res.category.toString().match(this.category.toString());
      });
    }else {
      this.ngOnInit();
    }
  }

}
