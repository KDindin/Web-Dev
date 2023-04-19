import { TestBed } from '@angular/core/testing';

import { AllService } from './company.service';

describe('CompanyService', () => {
  let service: AllService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AllService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
