"""Original exact exponent and log-coordinate domain controls.

All reported scale algebra uses Fraction; floats are used only for plotting.
Unity prefactors define illustrative boundaries, not physical calibrations.
No independent verifier is imported or executed, and no source PDF is read.
"""
from __future__ import annotations

import argparse
import csv
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys

ROOT=Path(__file__).resolve().parents[1]
TITLE='Scale ordering in localized tearing-mediated relativistic turbulence'
SOURCE={
    'title':'Tearing-mediated Alfvénic Turbulence in a Relativistic Plasma',
    'authors':['Stanislav Boldyrev','Nuno F. Loureiro'],
    'DOI':'10.3847/1538-4357/ada28a',
    'supplied_PDF_sha256':'c03eb1d83e8f01c3c7283973ed0a6d0b545b7b30ecc7c53b2996e039b9e1c1f6',
    'publisher_browser_math_sha256':'91db428fd02ef93bb27f254821991e89405489a7953d624d1743c0d597af2c83',
    'semantics':'Recorded provenance of supplied PDF and human-cleared publisher math; this offline producer does not rehash source bytes or assert fresh publisher-PDF identity.',
}

def sha(data):return hashlib.sha256(data).hexdigest()
def exact(value):return str(F(value))

def profile(n):
    if n not in (1,2):raise ValueError('Only the two source profile classes are used.')
    # Adopted aligned-cascade time exponent and fastest tearing rate.
    alignment=F(1,4)
    fastest_epsilon=F(1)+F(1,n)
    onset=alignment/(alignment+fastest_epsilon)
    amplitude=(F(2)+F(1,n))/3
    charge_x=2*amplitude-2
    # Equality of pre-tearing and tearing-mediated amplitude at onset.
    assert (onset-1)/4==-F(1,3)+amplitude*onset
    threshold=F(2,3)-charge_x*onset
    assert onset==F(n,4+5*n)
    assert amplitude==F(2*n+1,3*n)
    assert charge_x==-F(2*(n-1),3*n)
    assert threshold==F(2+4*n,4+5*n)
    assert 3*amplitude==2+F(1,n)  # constant energy flux
    return {'n':n,'onset_R_exponent':onset,
            'post_amplitude_x_exponent':amplitude,
            'one_dimensional_spectrum_exponent':-(2*amplitude+1),
            'post_charge_x_exponent':charge_x,
            'onset_sigma_threshold_R_exponent':threshold}

def case(n,logR,log_sigma):
    """Every scale is represented by its exact base-ten logarithm."""
    p=profile(n);r,s=F(logR),F(log_sigma)
    if r<=0:raise ValueError('R=L_perp/d_rel must exceed one in these examples.')
    xt=p['onset_R_exponent']*r
    xch=-r/3+2*s/3
    c_at=s-F(2,3)*r+p['post_charge_x_exponent']*xt
    c_d=s-F(2,3)*r
    star=3*s-2*r if n==2 else None
    assert c_at==s-p['onset_sigma_threshold_R_exponent']*r
    assert (xch<xt)==(c_at<0)
    assert (xch==xt)==(c_at==0)
    # Pre-tearing demand is sigma R^-1/2 x^-3/2.
    assert s-r/2-F(3,2)*xch==0
    assert s-r/2-F(3,2)*xt==c_at
    if c_at>0:
        regime='initial_charge_crossing_before_tearing_onset'
        post_valid=False
    elif c_at==0:
        regime='coincident_initial_thresholds_no_scale_separation'
        post_valid=False
    elif n==1:
        regime='Harris_tearing_first_no_post_tearing_crossing'
        post_valid=True
        assert p['post_charge_x_exponent']==0 and c_d==c_at<0
    elif c_d<0:
        regime='localized_tearing_first_secondary_crossing_below_d'
        post_valid=True
        assert star<0
    elif c_d==0:
        regime='localized_tearing_first_secondary_crossing_at_d'
        post_valid=True
        assert star==0
    else:
        regime='localized_tearing_first_secondary_crossing_above_d'
        post_valid=True
        assert 0<star<xt
        assert s-F(2,3)*r+p['post_charge_x_exponent']*star==0
    return {'n':n,'log10_R':r,'log10_sigma_tilde':s,
            'sigma_power_of_R':s/r,'log10_x_t':xt,
            'log10_x_ch_unmodified':xch,
            'log10_C_at_onset':c_at,'log10_C_at_d_if_continued':c_d,
            'log10_x_star_if_localized':star,
            'post_tearing_branch_initially_below_current_threshold':post_valid,
            'regime_under_unity_prefactors':regime}

def encode(value):
    if isinstance(value,F):return str(value)
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    if isinstance(value,list):return [encode(v) for v in value]
    return value

def save_json(path,value):
    path.write_text(json.dumps(encode(value),indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8',newline='\n')

def save_csv(path,rows):
    assert rows
    with path.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n')
        writer.writeheader()
        for row in rows:writer.writerow({k:exact(v) if isinstance(v,F) else '' if v is None else v for k,v in row.items()})

def figures(output):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
        'axes.labelsize':12,'axes.titlesize':12,'xtick.labelsize':10.5,
        'ytick.labelsize':10.5,'legend.fontsize':10.5,
        'axes.spines.top':False,'axes.spines.right':False,
        'savefig.facecolor':'white','figure.facecolor':'white'})
    blue='#14566b';orange='#b65305';green='#31786b';gray='#e7e9ec'
    # Coordinates are log10 values. No enormous R or sigma is converted to float.
    r=np.linspace(0,140,501);lower=2*r/3;upper=5*r/7
    fig,ax=plt.subplots(figsize=(9.0,5.35),layout='constrained')
    ax.fill_between(r,0,lower,color='#dceee8')
    ax.fill_between(r,lower,upper,color='#f8d39a')
    ax.fill_between(r,upper,110,color=gray)
    ax.plot(r,lower,color=blue,lw=2.1,label=r'$\widetilde\sigma=R^{2/3}$')
    ax.plot(r,upper,color=orange,lw=2.1,ls='--',label=r'$\widetilde\sigma=R^{5/7}$')
    ax.text(71,23,'Tearing first; no later crossing\nabove $d_{\\rm rel}$ in either profile model',ha='center',va='center',fontsize=11)
    ax.text(43,78,'Initial current-demand threshold\nis reached before localized tearing onset',ha='left',va='center',fontsize=11)
    ax.text(3,62,'Dots: formal exponent witnesses, not measured values',fontsize=10.4,
        bbox={'facecolor':'white','edgecolor':'none','alpha':.85})
    ax.annotate('Localized $n=2$: tearing first,\nthen a secondary crossing above $d_{\\rm rel}$',
        xy=(98,68),xytext=(47,53),ha='center',va='center',fontsize=10.7,
        arrowprops={'arrowstyle':'->','color':'#555555','lw':1.2},
        bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
    for m in (1,2,3):
        rr,ss=42*m,29*m
        ax.scatter([rr],[ss],color='#252525',s=27,zorder=5)
        ax.annotate(f'$m={m}$',(rr,ss),xytext=(7,4),textcoords='offset points',fontsize=10.5)
    ax.set(xlim=(0,140),ylim=(0,110),xlabel=r'$\log_{10}R$,  $R=L_\perp/d_{\rm rel}$',
        ylabel=r'$\log_{10}\widetilde\sigma$',title='Conditional scale domains for localized profiles (unity prefactors)')
    ax.legend(loc='upper left',framealpha=.95)
    ax.grid(alpha=.17)
    fig.savefig(output/'figures/phase-domains.png',dpi=220,metadata={'Author':'Taylor Kalin','Software':'Matplotlib'})
    plt.close(fig)

    fig,ax=plt.subplots(figsize=(9.0,4.95),layout='constrained')
    r=F(42);ut=profile(2)['onset_R_exponent']*r
    u=np.linspace(float(ut),0,401)
    # Localized case below both thresholds: all displayed continuation is valid
    # relative to this particular current-demand constraint.
    s=F(26);safe=float(s-F(2,3)*r)-u/3
    ax.plot(u,safe,color=blue,lw=2.4,label=r'$n=2,\ \log_{10}\widetilde\sigma=26$: no crossing')
    # Localized formal witness m=1: stop a solid model at C=1, then display an
    # explicitly dashed algebraic continuation rather than a physical prediction.
    star=F(3);u_before=np.linspace(float(ut),float(star),201);u_after=np.linspace(float(star),0,151)
    ax.plot(u_before,1-u_before/3,color=orange,lw=2.6,label=r'$n=2,\ \log_{10}\widetilde\sigma=29$: secondary crossing')
    ax.plot(u_after,1-u_after/3,color=orange,lw=2.1,ls='--',label='Formal continuation after the model boundary')
    # The Harris positive control is chosen below its own onset threshold.
    uh=np.linspace(float(profile(1)['onset_R_exponent']*r),0,201)
    ax.plot(uh,np.full_like(uh,-2),color=green,lw=2.3,ls='-.',label=r'$n=1,\ \log_{10}\widetilde\sigma=26$: constant demand')
    ax.axhline(0,color='#333333',lw=1.2)
    ax.axhspan(0,1.45,color='#f7e7df',alpha=.65,zorder=-1)
    ax.scatter([float(star)],[0],s=44,color=orange,zorder=6)
    ax.annotate(r'$x_*=10^3$',xy=(3,0),xytext=(4.1,.58),fontsize=11,
        arrowprops={'arrowstyle':'->','color':orange,'lw':1.2})
    ax.text(5.92,.12,'$C=1$: declared current-demand boundary',fontsize=10.4,va='bottom')
    ax.set(xlim=(6.1,-.12),ylim=(-4.5,1.45),xlabel=r'$\log_{10}x$,  $x=a/d_{\rm rel}$  (cascade toward smaller $x$ $\rightarrow$)',
        ylabel=r'$\log_{10}C(x)$',title=r'Synthetic post-tearing trajectories at $R=10^{42}$')
    ax.legend(loc='lower right',framealpha=.96)
    ax.grid(alpha=.18)
    fig.savefig(output/'figures/current-demand-trajectories.png',dpi=220,metadata={'Author':'Taylor Kalin','Software':'Matplotlib'})
    plt.close(fig)
    return {'python':platform.python_version(),'numpy':np.__version__,'matplotlib':matplotlib.__version__}

def main():
    if sys.flags.optimize:raise RuntimeError('Use ordinary Python without -O; exact guards must remain enabled.')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-root',type=Path,default=ROOT)
    args=parser.parse_args();out=args.output_root.resolve()
    for sub in ['data','figures']:(out/sub).mkdir(parents=True,exist_ok=True)
    profiles=[profile(1),profile(2)]
    rs=[3,6,12,30,42,84,126,210]
    ps=[F(-1,10),F(0),F(1,3),F(3,5),F(2,3),F(29,42),F(5,7),F(4,5),F(1)]
    finite=[case(n,r,p*r) for n in (1,2) for r in rs for p in ps]
    assert len(finite)==144
    transitions=[row for row in finite if row['log10_C_at_onset']==0 or (row['n']==2 and row['log10_C_at_d_if_continued']==0)]
    assert len(transitions)==24
    fixed_sigma=[row for row in finite if row['n']==2 and row['sigma_power_of_R']==0]
    assert len(fixed_sigma)==8
    assert all(row['log10_x_star_if_localized']==-2*row['log10_R'] for row in fixed_sigma)
    assert all(a['log10_x_star_if_localized']>b['log10_x_star_if_localized'] for a,b in zip(fixed_sigma,fixed_sigma[1:]))
    witnesses=[]
    for m in (1,2,3):
        row=case(2,42*m,29*m)
        assert row['log10_x_t']==6*m and row['log10_x_star_if_localized']==3*m
        assert row['log10_C_at_onset']==-m and row['log10_C_at_d_if_continued']==m
        assert row['log10_x_ch_unmodified']==F(16*m,3)
        assert row['regime_under_unity_prefactors']=='localized_tearing_first_secondary_crossing_above_d'
        witnesses.append({'m':m,**row,'log10_x_star_over_x_t':-3*m,
            'log10_sigma_over_R_two_thirds':m,
            'log10_R_five_sevenths_over_sigma':m,
            'interpretation':'Formal exponent witness, not an astrophysical measurement or complete physical admissibility claim.'})
    # Check the data used in the second figure by the exact classifier.
    plot_cases=[case(2,42,26),case(2,42,29),case(1,42,26)]
    assert plot_cases[0]['log10_C_at_d_if_continued']==-2
    assert plot_cases[1]['log10_x_star_if_localized']==3
    assert plot_cases[2]['log10_C_at_onset']==plot_cases[2]['log10_C_at_d_if_continued']==-2
    save_csv(out/'data/profile-exponents.csv',profiles)
    save_csv(out/'data/finite-domain-cases.csv',finite)
    save_csv(out/'data/transition-cases.csv',transitions)
    save_csv(out/'data/formal-witnesses.csv',witnesses)
    save_csv(out/'data/trajectory-cases.csv',plot_cases)
    locators={'source':SOURCE,'notation':{'R':'L_perp/d_rel > 1','x':'a/d_rel','C':'sigma_tilde*(b_a/b0)^2*x^-2'},
        'equations':{'onset':'Eqs.(7),(9)-(13), p.3','unmodified_charge_scale':'Eqs.(14)-(20), pp.3-4',
            'post_tearing_amplitude_and_spectrum':'Eqs.(21)-(24), p.4','localized_secondary_crossing':'Eq.(25), p.4',
            'source_conditional_caveat':'Paragraph immediately after Eq.(25), p.4','broader_summary':'Abstract p.1 and conclusion Eqs.(27)-(33), p.5'},
        'source_caveat_credited':'The source already expects a_star<d_rel in astrophysical systems and conditions its negligible-charge-starvation conclusion on that expectation.',
        'prefactor_policy':'Every omitted scale prefactor is set to unity only for declared synthetic estimates; boundaries are not measured physical transition calibrations.',
        'physical_outcome_not_computed':True}
    save_json(out/'data/producer-source-locators.json',locators)
    environment=figures(out)
    generated=[
        'data/profile-exponents.csv','data/finite-domain-cases.csv','data/transition-cases.csv',
        'data/formal-witnesses.csv','data/trajectory-cases.csv','data/producer-source-locators.json',
        'figures/phase-domains.png','figures/current-demand-trajectories.png']
    artifacts=[{'path':name,'bytes':(out/name).stat().st_size,'sha256':sha((out/name).read_bytes())} for name in generated]
    counts={regime:sum(row['regime_under_unity_prefactors']==regime for row in finite) for regime in sorted({r['regime_under_unity_prefactors'] for r in finite})}
    result={'schema_version':1,'status':'pass','title':TITLE,'author':'Taylor Kalin',
        'scientific_assessment':'qualified_or_inconclusive_findings; source-specific domain clarification, no demonstrated core algebra error',
        'producer_sha256':sha(Path(__file__).read_bytes()),'environment':environment,
        'exact_exponent_profiles':profiles,'finite_log_grid':{'log10_R':rs,'sigma_R_powers':ps,'cases':len(finite),'regime_counts':counts},
        'transition_equality_cases':len(transitions),'formal_witnesses':witnesses,'figure_trajectory_controls':plot_cases,
        'formal_limit':{'family':'R=10^(42m), sigma_tilde=10^(29m), m positive integer',
            'log10_x_t':'6m','log10_x_star':'3m','log10_C_at_onset':'-m','log10_C_at_d_if_continued':'m',
            'log10_x_star_over_x_t':'-3m','onset_demand_tends_to_zero':True},
        'localized_window_width':{'sigma_upper_over_lower':'R^(1/21)',
            'each_midpoint_magnetization_margin':'R^(1/42)',
            'both_margins_greater_than_K_require':'R>K^42',
            'finite_window_limit':'Finite prefactors can matter substantially; the formal family is not an inferred astrophysical parameter set.'},
        'fixed_magnetization_limit':{'identity':'x_star=sigma_tilde^3*R^-2 tends to zero at fixed sigma_tilde',
            'exact_grid_controls_at_sigma_equal_one':len(fixed_sigma),
            'formal_witnesses_use_correlated_double_scaling':True,
            'source_fixed_parameter_expectation_contradicted':False},
        'formulae':{'onset':'x_t=R^[n/(4+5n)]','unmodified_charge_scale':'x_ch=R^(-1/3)*sigma_tilde^(2/3)',
            'post_tearing_charge_demand':'C=sigma_tilde*R^(-2/3)*x^[-2(n-1)/(3n)]',
            'localized_secondary_scale':'x_star=sigma_tilde^3/R^2','n1_control':'C independent of x'},
        'source_caveat_credited':locators['source_caveat_credited'],'unity_prefactors_declared':True,
        'all_scientific_algebra_exact_Fraction':True,'large_values_never_exponentiated_for_plotting':True,
        'independent_verifier_imported_or_run':False,'artifacts':artifacts,
        'limits':['Conditional scale classification of the source phenomenology, not an algebra-error claim against Eq.(18) or Eq.(25).',
            'All examples are formal/synthetic; no measured astrophysical parameters or new source simulations are supplied.',
            'Unmodified x_ch below d_rel is only an algebraic extrapolation; the source footnote4 assumes that scale is above d_rel for its initial-cascade discussion.',
            'No post-crossing spectrum, heating, reconnection rate or kinetic outcome is predicted. Dashed extrapolation only illustrates where the assumed continuation fails its current-demand condition.',
            'Fixed d_rel, density, cascade flux, profile class and negligible competing damping/radiation remain assumptions. Broader physical admissibility must be checked independently.',
            'The Appendix algebra passed separate controls; no new full inner-ODE reconstruction is claimed.',
            'Unity-prefactor equalities mark illustrative boundaries; asymptotic << statements require separation from those boundaries.'],
        'new_PIC_MHD_or_full_inner_ODE_runs':0,'publication_or_freeze_claimed':False}
    save_json(out/'data/producer-results.json',result)
    print(json.dumps({'status':'pass','profiles':2,'finite_cases':144,'transition_cases':24,
        'formal_witnesses':3,'figures':2,'source_caveat_credited':True,
        'result_sha256':sha((out/'data/producer-results.json').read_bytes())}))

if __name__=='__main__':main()
