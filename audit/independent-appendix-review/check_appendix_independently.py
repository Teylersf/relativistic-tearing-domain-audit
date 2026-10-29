"""Bounded independent Appendix A algebra/special-function controls.

No author code, full eigenmode computation, simulation, network or publication.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,itertools,json,math,platform
import mpmath as mp

HERE=Path(__file__).resolve().parent
PROJECT=Path(__file__).resolve().parents[2]
RECORDED={row["filename"]:row for row in json.loads((PROJECT/"source-provenance.json").read_text(encoding="utf-8"))["source_inputs"]}
if not __debug__:raise RuntimeError('Run without -O; exact checks must remain enabled.')
mp.mp.dps=80

def main():
 exact_counts={'A1_A2_to_A3_operator_derivative':0,'A30_to_A31_change_of_variables':0,'A8_A15_solve_A7':0}
 for lam,beta,eps,x in itertools.product([F(1,100),F(2,13),F(5,7)],[F(1,3),F(3)],[F(1,50),F(2,9)],[F(1,19),F(1,2),F(7,3)]):
  # Arbitrary local phi' through phi'''' jets; psi'' eliminated by A2.
  y,yp,ypp,yppp=F(2,7),F(-3,5),F(7,11),F(-5,13)
  A=lam**2/x+beta**2*x;Ap=-lam**2/x**2+beta**2;App=2*lam**2/x**3
  r1_second=-lam**2*yp/x-2*y-x*yp+eps**2*(App*yp+2*Ap*ypp+A*yppp)
  r3_derivative=eps**2*((lam**2+beta**2*x*x)*yppp+(2*beta**2*x-2*lam**2/x)*ypp+2*lam**2/x**2*yp)-(lam**2+x*x)*yp-2*x*y
  assert r3_derivative==x*r1_second
  exact_counts['A1_A2_to_A3_operator_derivative']+=1
  # Independent direct chain-rule substitution into the two residuals.
  h,hz,hzz=F(5,3),F(-2,5),F(7,4)
  z=-beta**2*x*x/lam**2;zx=-2*beta**2*x/lam**2;zxx=-2*beta**2/lam**2
  Y=h-1/lam;Yp=hz*zx;Ypp=hzz*zx*zx+hz*zxx
  r30=(lam**2+beta**2*x*x)*eps**2*Ypp-2*lam**2*eps**2/x*Yp-lam**2*Y-lam
  r31=z*(1-z)*hzz-(1+z)/2*hz+lam**2/(4*beta**2*eps**2)*h
  assert r30==-4*beta**2*eps**2*r31
  exact_counts['A30_to_A31_change_of_variables']+=1
  denom=lam**2+beta**2*x*x
  deriv=-lam*x/(eps**2*denom)
  second=-lam*(lam**2-beta**2*x*x)/(eps**2*denom**2)
  assert eps**2*denom*second-2*lam**2*eps**2/x*deriv==lam
  exact_counts['A8_A15_solve_A7']+=1
 integral_rows=[]
 for beta,eps in itertools.product([mp.mpf('.2'),mp.mpf(1),mp.mpf(3)],[mp.mpf('.01'),mp.mpf('.07')]):
  lam=beta*eps*mp.mpf('.003');width=lam/beta
  fn=lambda x:-lam/(eps**2*(lam**2+beta**2*x*x))
  value=mp.quad(fn,[-mp.inf,-10*width,-width,0,width,10*width,mp.inf])
  target=-mp.pi/(beta*eps**2)
  error=abs(value/target-1);assert error<mp.mpf('1e-65')
  delta=-lam*value;recovered=beta*eps**2*delta/mp.pi
  assert abs(recovered/lam-1)<mp.mpf('1e-65')
  integral_rows.append({'beta_s':float(beta),'d_over_a':float(eps),'lambda':float(lam),'integral_relative_error':mp.nstr(error,20),'A23_recovers_lambda':True})
 # A10 and A12 evaluated independently with their different integral forms.
 match_rows=[];max_integral_difference=mp.mpf(0)
 for u in map(mp.mpf,['.01','.1','1','4']):
  q=mp.mpf('.07');C=mp.mpf('.31')
  tail=mp.quad(lambda v:mp.log(v)*mp.exp(u-v),[u,mp.inf])
  head=mp.quad(lambda v:mp.log(v)*mp.exp(v-u),[0,u])
  a10=-q*mp.log(u)+q*(tail+head)/2+C*mp.exp(-u)
  inner=mp.quad(lambda v:mp.log(v)*mp.sinh(v-u),[0,u])
  a12=-q*mp.log(u)-mp.euler*q*mp.exp(u)/2+q*inner+C*mp.exp(-u)
  error=abs(a10-a12);max_integral_difference=max(max_integral_difference,error)
  assert error<mp.mpf('1e-65')
  # The source constants match constant and linear overlap coefficients.
  eps=mp.mpf('.01');beta=mp.mpf(1);lam=mp.mpf('.0001');q0=lam/(beta**2*eps**2)
  CI=q0*(mp.log(beta**2*eps/lam)-mp.euler);CII=-mp.euler*q0/2
  constant_I=CI-q0*mp.log(beta/lam)
  constant_II=q0*mp.log(beta*eps)-mp.euler*q0/2+CII
  linear_II=(-mp.euler*q0/2-CII)/(beta*eps)
  assert abs(constant_I-constant_II)<mp.mpf('1e-65') and linear_II==0
  match_rows.append({'scaled_xi':float(u),'A10_A12_absolute_difference':mp.nstr(error,20)})
 # Exact hypergeometric connection formula A36 at negative real z.
 hyper_rows=[];max_hyper_error=mp.mpf(0)
 for alpha,z in itertools.product(map(mp.mpf,['.001','.01','.1','.3']),map(mp.mpf,['-2','-10','-100','-10000'])):
  b=-mp.mpf('.5')-alpha;c=-mp.mpf('.5')
  direct=mp.hyp2f1(alpha+1,b+1,c+1,z)
  first=mp.gamma(b-alpha)*mp.gamma(c+1)/(mp.gamma(b+1)*mp.gamma(c-alpha))*(-z)**(-alpha-1)*mp.hyp2f1(alpha+1,alpha-c+1,alpha-b+1,1/z)
  second=mp.gamma(alpha-b)*mp.gamma(c+1)/(mp.gamma(alpha+1)*mp.gamma(c-b))*(-z)**(-b-1)*mp.hyp2f1(b+1,b-c+1,b-alpha+1,1/z)
  error=abs((first+second)/direct-1);max_hyper_error=max(max_hyper_error,error)
  assert error<mp.mpf('1e-65')
  r=4*alpha**2+2*alpha
  assert abs(alpha*b/c-r/2)<mp.mpf('1e-70')
  hyper_rows.append({'alpha':float(alpha),'z':float(z),'A36_relative_error':mp.nstr(error,20),'A35_prefactor_identity':True})
 coefficients=[]
 for alpha in map(mp.mpf,['.01','.001','.0001']):
  b=-mp.mpf('.5')-alpha;c=-mp.mpf('.5')
  coefficient_A=mp.gamma(c)*mp.gamma(b-alpha)/(mp.gamma(b)*mp.gamma(c-alpha))
  coefficient_B=mp.gamma(c)*mp.gamma(alpha-b)/(mp.gamma(alpha)*mp.gamma(c-b))
  coefficients.append({'alpha':float(alpha),'A39_first_coefficient':mp.nstr(coefficient_A,25),'A39_second_coefficient_over_minus_2pi_alpha_squared':mp.nstr(coefficient_B/(-2*mp.pi*alpha**2),25)})
 assert abs(mp.mpf(coefficients[-1]['A39_first_coefficient'])-1)<abs(mp.mpf(coefficients[0]['A39_first_coefficient'])-1)
 assert abs(mp.mpf(coefficients[-1]['A39_second_coefficient_over_minus_2pi_alpha_squared'])-1)<abs(mp.mpf(coefficients[0]['A39_second_coefficient_over_minus_2pi_alpha_squared'])-1)
 overlap=[]
 for beta in map(mp.mpf,['1','.1','.01']):
  eps=mp.mpf('.001');delta=beta*mp.mpf('.01')/eps;lam=beta*eps**2*delta/mp.pi
  ratio=(lam/beta)/(beta*eps)
  assert abs(ratio-mp.mpf('.01')/mp.pi)<mp.mpf('1e-70')
  overlap.append({'beta_s':float(beta),'epsilon_Delta_prime':float(eps*delta),'lower_over_upper_overlap_scale':float(ratio)})
 scalings=[]
 for n in [1,2]:
  # A17 plus the low/high-beta fastest-mode crossovers.
  eps_exp=F(1)+F(1,n);beta_exp=F(2,3)+F(1,3*n)
  assert eps_exp==F(n+1,n) and beta_exp==F(2*n+1,3*n)
  scalings.append({'n':n,'A20_epsilon_exponent':str(eps_exp),'A45_beta_s_exponent':str(beta_exp)})
 report={'schema_version':1,'status':'pass',
  'source_title':'Tearing-mediated Alfvénic Turbulence in a Relativistic Plasma','source_DOI':'10.3847/1538-4357/ada28a',
  'source_inputs':{'supplied_PDF_sha256':RECORDED["supplied.pdf"]["sha256"],'publisher_browser_TeX_sha256':RECORDED["journal-browser-math-tex.json"]["sha256"],'fresh_journal_PDF_byte_identity_asserted':False,'source_bytes_rehashed_this_run':False},
  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'environment':{'python':platform.python_version(),'mpmath':mp.__version__,'mpmath_digits':80},
  'exact_fraction_control_counts':exact_counts,'A15_A23_integrals':integral_rows,'A10_A14_controls':match_rows,'maximum_A10_A12_absolute_difference':mp.nstr(max_integral_difference,20),
  'A36_connection_controls':hyper_rows,'maximum_A36_relative_difference':mp.nstr(max_hyper_error,20),'A39_asymptotic_coefficient_controls':coefficients,
  'pressure_branch_overlap_controls':overlap,'fastest_rate_exponent_controls':scalings,
  'qualifications':['A16/A23 result from a leading inner approximation extended in matching; no exact finite-parameter full-eigenmode coefficient claim.',
   'For positive real xi, z=-beta_s^2*xi^2/lambda^2 is negative; prose z>>1 means large magnitude, with the displayed (-z) formulas used on that physical branch.',
   'Strict overlap requires lambda/beta_s << beta_s*d/a, not just an order-one crossover bound.',
   'Large-beta formal extension also needs an inner-to-sheet scale ordering; no uniform accuracy at a finite-beta dispersion pole established.',
   'The alpha-dependent logarithmic tail requires a controlled cutoff/ordering; this check does not allege an actual leading-scaling error.'],
  'scope':'Appendix-only algebra, matching and special-function checks. No full ODE eigenmode, source simulation, author code, network or publication.'}
 (HERE/'independent-appendix-checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({'status':'pass','exact_groups':exact_counts,'A15_integrals':len(integral_rows),'A36_cases':len(hyper_rows),'max_A36_error':mp.nstr(max_hyper_error,20),'receipt_sha256':hashlib.sha256((HERE/'independent-appendix-checks.json').read_bytes()).hexdigest()}))

if __name__=='__main__':main()
