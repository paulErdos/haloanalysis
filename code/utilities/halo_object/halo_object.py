class Halo:
  def __init__(self, scale_0, id_1, desc_scale_2, desc_id_3, num_prog_4, pid_5, upid_6, desc_pid_7, phantom_8, sam_mvir_9, mvir_10, rvir_11, rs_12, vrms_13, is_mmp_14, scale_of_last_MM_15, vmax_16, x_17, y_18, z_19, vx_20, vy_21, vz_22, Jx_23, Jy_24, Jz_25, Spin_26, Breadth_first_ID_27, Depth_first_ID_28, Tree_root_ID_29, Orig_halo_ID_30, Snap_num_31, Next_coprogenitor_depthfirst_ID_32, Last_progenitor_depthfirst_ID_33, Last_mainleaf_depthfirst_ID_34, Tidal_Force_35, Tidal_ID_36, Rs_Klypin_37, Mvir_all_38, M200b_39, M200c_40, M500c_41, M2500c_42, Xoff_43, Voff_44, Spin_Bullock_45, b_to_a_46, c_to_a_47, A_x_48, A_y_49, A_z_50, b_to_a_500c_51, c_to_a_500c_52, A_x_500c_53, A_y_500c_54, A_z_500c_55, T_per_magnitude_U_56, M_pe_Behroozi_57, M_pe_Diemer_58, Macc_59, Mpeak_60, Vacc_61, Vpeak_62, Halfmass_Scale_63, Acc_Rate_Inst_64, Acc_Rate_100Myr_65, Acc_Rate_x_Tdyn_66, Acc_Rate_x_2Tdyn_67, Acc_Rate_Mpeak_68, Mpeak_Scale_69, Acc_Scale_70, First_Acc_Scale_71, First_Acc_Mvir_72, First_Acc_Vmax_73, Vmax_at_Mpeak_74, Tidal_Force_Tdyn_75, wall1, wall2, wall3, fila1, fila2, fila3, dist1, dist2, dist3):

    #Scale: Scale factor of halo.
    self.scale_0 = scale_0

    #ID: ID of halo (unique across entire simulation).
    self.id_1 = id_1

    #Desc_Scale: Scale of descendant halo, if applicable.
    self.desc_scale_2 = desc_scale_2

    #Descid: ID of descendant halo, if applicable.
    self.desc_id_3 = desc_id_3

    #Num_prog: Number of progenitors.
    self.num_prog_4 = num_prog_4

    #Pid: ID of least massive host halo (-1 if distinct halo).
    self.pid_5 = pid_5

    #Upid: ID of most massive host halo (different from Pid 
    #when the halo is within two or more larger halos).
    self.upid_6 = upid_6

    #Desc_pid: Pid of descendant halo (if applicable).
    self.desc_pid_7 = desc_pid_7

    #Phantom: Nonzero for halos interpolated across timesteps.
    self.phantom_8 = phantom_8

    #SAM_Mvir: Halo mass, smoothed across accretion history;
    #always greater than sum of halo masses of contributing
    #progenitors (Msun/h).  Only for use with select
    #semi-analytic models.
    self.sam_mvir_9 = sam_mvir_9

    #Mvir: Halo mass (Msun/h).
    self.mvir_10 = mvir_10

    #Rvir: Halo radius (kpc/h comoving).
    self.rvir_11 = rvir_11

    #Rs: Scale radius (kpc/h comoving).
    self.rs_12 = rs_12

    #Vrms: Velocity dispersion (km/s physical).
    self.vrms_13 = vrms_13

    #is_mmp: whether the halo is the most massive progenitor 
    #or not.
    self.is_mmp_14 = is_mmp_14

    #scale_of_last_MM: scale factor of the last major merger 
    #(Mass ratio > 0.3).
    self.scale_of_last_MM_15 = scale_of_last_MM_15

    #Vmax: Maxmimum circular velocity (km/s physical).
    self.vmax_16 = vmax_16

    #X/Y/Z: Halo position (Mpc/h comoving).
    self.x_17 = x_17

    #X/Y/Z: Halo position (Mpc/h comoving).
    self.y_18 = y_18

    #X/Y/Z: Halo position (Mpc/h comoving).
    self.z_19 = z_19

    #VX/VY/VZ: Halo velocity (km/s physical).
    self.vx_20 = vx_20

    #VX/VY/VZ: Halo velocity (km/s physical).
    self.vy_21 = vy_21

    #VX/VY/VZ: Halo velocity (km/s physical).
    self.vz_22 = vz_22

    #JX/JY/JZ: Halo angular momenta 
    #((Msun/h) * (Mpc/h) * km/s (physical)).
    self.Jx_23 = Jx_23

    #JX/JY/JZ: Halo angular momenta 
    #((Msun/h) * (Mpc/h) * km/s (physical)).
    self.Jy_24 = Jy_24

    #JX/JY/JZ: Halo angular momenta 
    #((Msun/h) * (Mpc/h) * km/s (physical)).
    self.Jz_25 = Jz_25

    #Spin: Halo spin parameter.
    self.Spin_26 = Spin_26

    #Breadth_first_ID: breadth-first ordering of halos within 
    #a tree.
    self.Breadth_first_ID_27 = Breadth_first_ID_27

    #Depth_first_ID: depth-first ordering of halos within a 
    #tree.
    self.Depth_first_ID_28 = Depth_first_ID_28

    #Tree_root_ID: ID of the halo at the last timestep in the 
    #tree.
    self.Tree_root_ID_29 = Tree_root_ID_29

    #Orig_halo_ID: Original halo ID from halo finder.
    self.Orig_halo_ID_30 = Orig_halo_ID_30

    #Snap_num: Snapshot number from which halo originated.
    self.Snap_num_31 = Snap_num_31

    #Next_coprogenitor_depthfirst_ID: Depthfirst ID of next 
    #coprogenitor.
    self.Next_coprogenitor_depthfirst_ID_32 = Next_coprogenitor_depthfirst_ID_32

    #Last_progenitor_depthfirst_ID: Depthfirst ID of last 
    #progenitor.
    self.Last_progenitor_depthfirst_ID_33 = Last_progenitor_depthfirst_ID_33

    #Last_mainleaf_depthfirst_ID: Depthfirst ID of last 
    #progenitor on main progenitor branch.
    self.Last_mainleaf_depthfirst_ID_34 = Last_mainleaf_depthfirst_ID_34

    #Tidal_Force: Strongest tidal force from any nearby halo, 
    #in dimensionless units (Rhalo / Rhill).
    self.Tidal_Force_35 = Tidal_Force_35

    #Tidal_ID: ID of halo exerting strongest tidal force.
    self.Tidal_ID_36 = Tidal_ID_36

    #Rs_Klypin: Scale radius determined using Vmax and Mvir 
    #(see Rockstar paper)
    self.Rs_Klypin_37 = Rs_Klypin_37

    #Mvir_all: Mass enclosed within the specified overdensity,
    #including unbound particles (Msun/h)
    self.Mvir_all_38 = Mvir_all_38

    #M200b--M2500c: Mass enclosed within specified 
    #overdensities (Msun/h)
    self.M200b_39 = M200b_39

    #M200b--M2500c: Mass enclosed within specified 
    #overdensities (Msun/h)
    self.M200c_40 = M200c_40

    #M200b--M2500c: Mass enclosed within specified 
    #overdensities (Msun/h)
    self.M500c_41 = M500c_41

    #M200b--M2500c: Mass enclosed within specified 
    #overdensities (Msun/h)
    self.M2500c_42 = M2500c_42

    #Xoff: Offset of density peak from average particle 
    #position (kpc/h comoving)
    self.Xoff_43 = Xoff_43

    #Voff: Offset of density peak from average particle 
    #velocity (km/s physical)
    self.Voff_44 = Voff_44

    #Spin_Bullock: Bullock spin parameter (J/(sqrt(2)*GMVR))
    self.Spin_Bullock_45 = Spin_Bullock_45

    #b_to_a, c_to_a: Ratio of second and third largest shape
    #ellipsoid axes (B and C) to largest shape ellipsoid axis 
    #(A) (dimensionless). Shapes are determined by the method
    #in Allgood et al. (2006)  (500c) indicates that only 
    #particles within R500c are considered.
    self.b_to_a_46 = b_to_a_46

    #b_to_a, c_to_a: Ratio of second and third largest shape 
    #ellipsoid axes (B and C) to largest shape ellipsoid axis 
    #(A) (dimensionless). Shapes are determined by the method 
    #in Allgood et al. (2006)  (500c) indicates that only 
    #particles within R500c are considered.
    self.c_to_a_47 = c_to_a_47

    #A[x],A[y],A[z]: Largest shape ellipsoid axis 
    #(kpc/h comoving)
    self.A_x_48 = A_x_48

    #A[x],A[y],A[z]: Largest shape ellipsoid axis 
    #(kpc/h comoving)
    self.A_y_49 = A_y_49

    #A[x],A[y],A[z]: Largest shape ellipsoid axis 
    #(kpc/h comoving)
    self.A_z_50 = A_z_50

    #b_to_a, c_to_a: Ratio of second and third largest shape 
    #ellipsoid axes (B and C) to largest shape ellipsoid axis 
    #(A) (dimensionless). Shapes are determined by the method 
    #in Allgood et al. (2006)  (500c) indicates that only 
    #particles within R500c are considered.
    self.b_to_a_500c_51 = b_to_a_500c_51

    #b_to_a, c_to_a: Ratio of second and third largest shape 
    #ellipsoid axes (B and C) to largest shape ellipsoid axis 
    #(A) (dimensionless). Shapes are determined by the method 
    #in Allgood et al. (2006)  (500c) indicates that only 
    #particles within R500c are considered.
    self.c_to_a_500c_52 = c_to_a_500c_52

    #(500c) indicates that only particles within R500c are 
    #considered.
    self.A_x_500c_53 = A_x_500c_53

    #(500c) indicates that only particles within R500c are 
    #considered.
    self.A_y_500c_54 = A_y_500c_54

    #(500c) indicates that only particles within R500c are 
    #considered.
    self.A_z_500c_55 = A_z_500c_55

    #T/|U|: ratio of kinetic to potential energies
    self.T_per_magnitude_U_56 = T_per_magnitude_U_56

    #M_pe_*: Pseudo-evolution corrected masses 
    #(very experimental) Consistent Trees Version 1.01. 
    #Includes fix for Rockstar spins & T/|U| 
    #(assuming T/|U| = column 53)
    self.M_pe_Behroozi_57 = M_pe_Behroozi_57

    #M_pe_*: Pseudo-evolution corrected masses 
    #(very experimental) Consistent Trees Version 1.01. 
    #Includes fix for Rockstar spins & T/|U| 
    #(assuming T/|U| = column 53)
    self.M_pe_Diemer_58 = M_pe_Diemer_58

    #Macc: Mass at accretion
    self.Macc_59 = Macc_59

    #Mpeak: Peak mass over mass accretion history.
    self.Mpeak_60 = Mpeak_60

    #Vacc: Vmax at accretion
    self.Vacc_61 = Vacc_61

    #Vpeak: Peak Vmax over mass accretion history.
    self.Vpeak_62 = Vpeak_62

    #Halfmass_Scale: Scale factor at which the MMP reaches 
    #0.5*Mpeak.
    self.Halfmass_Scale_63 = Halfmass_Scale_63

    #Acc_Rate_*: Halo mass accretion rates in Msun/h/yr. 
    #Inst: instantaneous; 100Myr: averaged over past 100Myr, 
    #X*Tdyn: averaged over past X*virial dynamical time. 
    #Mpeak: Growth Rate of Mpeak, averaged from current z to 
    #z+0.5
    self.Acc_Rate_Inst_64 = Acc_Rate_Inst_64

    #Acc_Rate_*: Halo mass accretion rates in Msun/h/yr. 
    #Inst: instantaneous; 100Myr: averaged over past 100Myr, 
    #X*Tdyn: averaged over past X*virial dynamical time. 
    #Mpeak: Growth Rate of Mpeak, averaged from current z to 
    #z+0.5
    self.Acc_Rate_100Myr_65 = Acc_Rate_100Myr_65

    #Acc_Rate_*: Halo mass accretion rates in Msun/h/yr. 
    #Inst: instantaneous; 100Myr: averaged over past 100Myr, 
    #X*Tdyn: averaged over past X*virial dynamical time. 
    #Mpeak: Growth Rate of Mpeak, averaged from current z to 
    #z+0.5
    self.Acc_Rate_x_Tdyn_66 = Acc_Rate_x_Tdyn_66

    #Acc_Rate_*: Halo mass accretion rates in Msun/h/yr. 
    #Inst: instantaneous; 100Myr: averaged over past 100Myr, 
    #X*Tdyn: averaged over past X*virial dynamical time. 
    #Mpeak: Growth Rate of Mpeak, averaged from current z to 
    #z+0.5
    self.Acc_Rate_x_2Tdyn_67 = Acc_Rate_x_2Tdyn_67


    #Acc_Rate_*: Halo mass accretion rates in Msun/h/yr. 
    #Inst: instantaneous; 100Myr: averaged over past 100Myr, 
    #X*Tdyn: averaged over past X*virial dynamical time. 
    #Mpeak: Growth Rate of Mpeak, averaged from current z to 
    #z+0.5
    self.Acc_Rate_Mpeak_68 = Acc_Rate_Mpeak_68

    #Mpeak_Scale: Scale at which Mpeak was reached.
    self.Mpeak_Scale_69 = Mpeak_Scale_69

    #Acc_Scale: Scale at which satellites were (last) accreted.
    self.Acc_Scale_70 = Acc_Scale_70

    #First_Acc_Scale: Scale at which current and former 
    #satellites first passed through a larger halo.
    self.First_Acc_Scale_71 = First_Acc_Scale_71

    #First_Acc_(Mvir|Vmax): Mvir and Vmax at First_Acc_Scale.
    self.First_Acc_Mvir_72 = First_Acc_Mvir_72

    #First_Acc_(Mvir|Vmax): Mvir and Vmax at First_Acc_Scale.
    self.First_Acc_Vmax_73 = First_Acc_Vmax_73

    #Vmax@Mpeak: Halo Vmax at the scale at which Mpeak was 
    #reached.
    self.Vmax_at_Mpeak_74 = Vmax_at_Mpeak_74

    #Tidal_Force_Tdyn: Dimensionless tidal force averaged 
    #over past dynamical time.
    self.Tidal_Force_Tdyn_75 = Tidal_Force_Tdyn_75

    #wall1: 1 if halo is inside wall @ 1Mpc smoothing
    self.wall1 = wall1

    #wall2: 1 if halo is inside wall @ 2Mpc smoothing
    self.wall2 = wall2

    #wall3: 1 if halo is inside wall @ 4Mpc smoothing
    self.wall3 = wall3

    #fila1: 1 if halo is inside filament @ 1Mpc smoothing
    self.fila1 = fila1

    #fila2: 1 if halo is inside filament @ 2Mpc smoothing
    self.fila2 = fila2

    #fila3: 1 if halo is inside filament @ 4Mpc smoothing
    self.fila3 = fila3

    #dist1: approx distance from halo to closest Spine elemenit
    #(wall, filament, cluster) @ 1Mpc smoothing. Units in 
    #voxels (250 Mpc)/(1024 pix)
    self.dist1 = dist1 

    #dist2: approx distance from halo to closest Spine elemenit
    #(wall, filament, cluster) @ 2Mpc smoothing. Units in 
    #voxels (250 Mpc)/(1024 pix)
    self.dist2 = dist2

    #dist3: approx distance from halo to closest Spine elemenit
    #(wall, filament, cluster) @ 4Mpc smoothing. Units in 
    #voxels (250 Mpc)/(1024 pix)
    self.dist3 = dist3 
