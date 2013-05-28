// Generated by CoffeeScript 1.4.0
(function() {
  var emptyAddr;

  window.App = angular.module('ldb', ['ldb.controllers', 'typeahead', 'dienst2.forms']).config([
    '$routeProvider', function($routeProvider) {
      $routeProvider.when('/dashboard', {
        templateUrl: window.prefix + 'partials/ldb/dashboard.html',
        controller: 'DashboardController'
      });
      $routeProvider.when('/person/new', {
        templateUrl: window.prefix + 'partials/ldb/person.html',
        controller: 'PersonDetailController'
      });
      $routeProvider.when('/person/:personID', {
        templateUrl: window.prefix + 'partials/ldb/person.html',
        controller: 'PersonDetailController'
      });
      $routeProvider.when('/organization/new', {
        templateUrl: window.prefix + 'partials/ldb/organization.html',
        controller: 'OrganizationDetailController'
      });
      $routeProvider.when('/organization/:organizationID', {
        templateUrl: window.prefix + 'partials/ldb/organization.html',
        controller: 'OrganizationDetailController'
      });
      $routeProvider.when('/export', {
        templateUrl: window.prefix + 'partials/ldb/export.html',
        controller: 'ExportController'
      });
      $routeProvider.otherwise({
        redirectTo: '/dashboard'
      });
    }
  ]);

  angular.module('ldb.controllers', ['ldb.apiv2']).controller('DashboardController', [
    '$scope', 'Person', 'Organization', function($scope, Person, Organization) {
      var classes, searchID;
      $scope.search = "";
      $scope.searchtype = "p";
      $scope.results = [];
      classes = {
        o: Organization,
        p: Person
      };
      searchID = 0;
      $scope.$watch('searchtype + search', function() {
        if ($scope.search.length > 1) {
          searchID++;
          return classes[$scope.searchtype].search($scope.search, function(results, status, headers, config) {
            if (config.params.searchID === searchID) {
              return $scope.results = results;
            }
          }, 'start', searchID);
        } else {
          return $scope.results = [];
        }
      });
      return $("#zoekbalk").focus();
    }
  ]).controller('PersonDetailController', [
    '$routeParams', '$location', '$scope', 'Person', 'Committee', 'CommitteeMembership', 'country_list', function($routeParams, $location, $scope, Person, Committee, CommitteeMembership, country_list) {
      $scope.country_list = country_list;
      $scope.editmode = false;
      $scope.committeelist = [];
      Committee.all(function(committeelist) {
        return $scope.committeelist = committeelist;
      });
      $scope.committeeFilter = function(committee) {
        return !committee._delete;
      };
      $scope.otherpersons = function(query, callback) {
        return Person.search(query, function(sources) {
          return callback(sources);
        }, 'start');
      };
      $scope.notLivingWith = function() {
        $scope.living_with_model = null;
        $scope.living_with = null;
        $scope.person.living_with_model = null;
        return $scope.person.living_with = null;
      };
      $scope.$watch('living_with_model', function() {
        var model;
        model = $scope.living_with_model;
        if (model && model.resource_uri) {
          $scope.person.living_with_model = model;
          return $scope.person.living_with = model.resource_uri;
        }
      });
      $scope.save = function() {
        $scope.person.saveAll(function(success) {
          return $location.path('/person/' + $scope.person.id);
        }, function(data, status, headers, config) {
          if (status === 400) {
            alert("Het formulier is niet geldig. \n \n" + angular.toJson(data));
            return $scope.editmode = true;
          }
        });
        return $scope.editmode = false;
      };
      $scope.removePerson = function() {
        return $scope.person.remove(function() {
          return $location.path('/dashboard');
        });
      };
      if ($routeParams.personID) {
        return Person.get($routeParams.personID, function(person) {
          $scope.person = person;
          return $scope.person.loadSubresources();
        });
      } else {
        $scope.person = new Person();
        $scope.person.loadSubresources();
        return $scope.editmode = true;
      }
    }
  ]).controller('OrganizationDetailController', [
    '$routeParams', '$location', '$scope', 'Organization', 'country_list', function($routeParams, $location, $scope, Organization, country_list) {
      $scope.country_list = country_list;
      $scope.editmode = false;
      $scope.save = function() {
        $scope.organization.save(function(success) {
          return $location.path('/organization/' + $scope.organization.id);
        }, function(data, status, headers, config) {
          if (status === 400) {
            alert("Het formulier is niet geldig. \n \n" + angular.toJson(data));
            return $scope.editmode = true;
          }
        });
        return $scope.editmode = false;
      };
      $scope.removeOrganization = function() {
        return $scope.organization.remove(function() {
          return $location.path('/dashboard');
        });
      };
      if ($routeParams.organizationID) {
        return Organization.get($routeParams.organizationID, function(organization) {
          return $scope.organization = organization;
        });
      } else {
        $scope.organization = new Organization();
        return $scope.editmode = true;
      }
    }
  ]).controller('ExportController', ['$scope', function($scope) {}]);

  emptyAddr = function() {
    return this.street_name = this.house_number = this.address_2 = this.address_3 = this.postcode = this.city = this.country = null;
  };

  angular.module('ldb.apiv2', ['dienst2']).factory('Member', [
    'Tastypie', function(Tastypie) {
      var Member;
      return Member = Tastypie('api/v2/member/');
    }
  ]).factory('Student', [
    'Tastypie', '$filter', function(Tastypie, $filter) {
      var Student;
      Student = Tastypie('api/v2/student/');
      Student.prototype.confirm = function() {
        var datefilter, today;
        today = new Date();
        datefilter = $filter('date');
        this.date_verified = datefilter(today, 'yyyy-MM-dd');
        if (this.resource_uri) {
          return this.update();
        }
      };
      return Student;
    }
  ]).factory('Alumnus', [
    'Tastypie', function(Tastypie) {
      var Alumnus;
      return Alumnus = Tastypie('api/v2/alumnus/');
    }
  ]).factory('Employee', [
    'Tastypie', function(Tastypie) {
      var Employee;
      return Employee = Tastypie('api/v2/employee/');
    }
  ]).factory('CommitteeMembership', [
    'Tastypie', function(Tastypie) {
      var CommitteeMembership;
      return CommitteeMembership = Tastypie('api/v2/committeeMembership/');
    }
  ]).factory('Person', [
    'Tastypie', 'Member', 'Student', 'Alumnus', 'Employee', 'CommitteeMembership', function(Tastypie, Member, Student, Alumnus, Employee, CommitteeMembership) {
      var Person, handleError, process;
      Person = Tastypie('api/v2/person/');
      Person.prototype.emptyAddr = emptyAddr;
      Person.prototype.toString = function() {
        var name;
        name = this.firstname;
        if (this.preposition) {
          name += " " + this.preposition;
        }
        name += " " + this.surname;
        return name;
      };
      Person.prototype.committeememberships = [];
      Person.prototype.loadSubresources = function(success) {
        var self, update;
        update = function() {
          if (success) {
            return success();
          }
        };
        self = this;
        Student.getSubresource(self.student, function(student) {
          if (!student) {
            student = new Student();
          }
          self.student_model = student;
          return update();
        });
        Member.getSubresource(self.member, function(member) {
          if (!member) {
            member = new Member();
          }
          self.member_model = member;
          return update();
        });
        Alumnus.getSubresource(self.alumnus, function(alumnus) {
          if (!alumnus) {
            alumnus = new Alumnus();
          }
          self.alumnus_model = alumnus;
          return update();
        });
        Employee.getSubresource(self.employee, function(employee) {
          if (!employee) {
            employee = new Employee();
          }
          self.employee_model = employee;
          return update();
        });
        Person.getSubresource(self.living_with, function(person) {
          self.living_with_model = person;
          return update();
        });
        if (self.committees) {
          return CommitteeMembership._more({
            method: 'GET',
            url: CommitteeMembership.api_root,
            params: {
              'limit': 0,
              'person': self.id
            }
          }, function(committeememberships) {
            self.committeememberships = committeememberships;
            return update();
          });
        }
      };
      handleError = function() {};
      process = function(obj, success, handleError) {
        if (obj._delete) {
          if (obj.resource_uri) {
            return obj.remove(success, handleError);
          }
        } else if (obj.changed()) {
          if (obj.resource_uri) {
            return obj.update(success, handleError);
          } else {
            return obj.create(success, handleError);
          }
        }
      };
      Person.prototype.newCommittee = function() {
        var committeemembership;
        committeemembership = new CommitteeMembership();
        committeemembership.person = this.resource_uri;
        return this.committeememberships.push(committeemembership);
      };
      Person.prototype.saveAll = function(success, error) {
        handleError = error;
        if (this.living_with_model) {
          this.living_with = this.living_with_model.resource_uri;
        }
        process(this.student_model);
        process(this.member_model);
        process(this.alumnus_model);
        process(this.employee_model);
        angular.forEach(this.committeememberships, function(obj) {
          return process(obj);
        });
        return process(this, function() {
          return success;
        });
      };
      return Person;
    }
  ]).factory('Organization', [
    'Tastypie', function(Tastypie) {
      var Organization;
      Organization = Tastypie('api/v2/organization/');
      Organization.prototype.emptyAddr = emptyAddr;
      Organization.prototype.save = function(success, error) {
        if (this.changed()) {
          if (this.resource_uri) {
            if (this._delete) {
              return this.remove(success, error);
            } else {
              return this.update(success, error);
            }
          } else {
            return this.create(success, error);
          }
        }
      };
      return Organization;
    }
  ]).factory('Committee', [
    'Tastypie', function(Tastypie) {
      var Committee;
      Committee = Tastypie('api/v2/committee/');
      Committee.prototype.toString = function() {
        return this.committeename;
      };
      Committee.all = function(success) {
        return Committee._more({
          method: 'GET',
          url: Committee.api_root,
          params: {
            'limit': 0
          }
        }, success);
      };
      return Committee;
    }
  ]);

}).call(this);
