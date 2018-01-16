import 'package:angular/angular.dart';
import 'package:angular_router/angular_router.dart';

import 'src/hero_service.dart';
import 'src/heroes_component.dart';
import 'src/dashboard_component.dart';
import 'src/hero_detail_component.dart';


@Component(
  selector: 'my-app',
  template: '''
    <h1>{{title}}</h1>
    <nav>
      <a [routerLink]="['Dashboard']">Dashboard</a>
      <a [routerLink]="['Heroes']">Heroes</a>
    </nav>
    <router-outlet></router-outlet>
  ''',
  directives: const [ROUTER_DIRECTIVES],
  providers: const [HeroService],
  styleUrls: const ['app_component.css'],
)

@RouteConfig(const [
  const Route(
      path: '/heroes',
      name: 'Heroes',
      component: HeroesComponent
  ),
  const Route(
      path: '/dashboard',
      name: 'Dashboard',
      component: DashboardComponent,
  ),
  const Route(
    path: '/detail/:id',
    name: 'HeroDetail',
    component: HeroDetailComponent,
  ),
  const Redirect(path: '/', redirectTo: const ['Dashboard']),
])

class AppComponent {
  final title = 'Tour of Heroes';
}
