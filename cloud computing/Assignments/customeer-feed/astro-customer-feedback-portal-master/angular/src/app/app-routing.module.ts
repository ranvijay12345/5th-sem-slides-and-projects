import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ReviewComponent } from './pages/review/review.component';
import { NewReviewComponent } from './pages/review/new-review/new-review.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';


const routes: Routes = [{
  path: 'review',
  component: ReviewComponent
}, {
  path: 'new-review',
  component: NewReviewComponent
}, {
  path: '',
  redirectTo: '/review',
  pathMatch: 'full'

}, {
  path: '**',
  component: PageNotFoundComponent
}]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
