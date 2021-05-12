import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {OfferComponent} from './offer/offer.component';
import {OfferDetailComponent} from './offer-detail/offer-detail.component';

const routes: Routes = [
  {path: '', component: OfferComponent},
  {path: 'offers/:id', component: OfferDetailComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
