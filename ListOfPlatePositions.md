
<strong style="color: red;">Development document, you don't normally need it for this robotics lab.</strong>

# Working with MCS
-	X with offset of about -210, direction: positive.
-	Y with offset pf about -80, direction: negative.
-	Z actually does not change.

# List of plate positions

See in projet: ``GVL_NestPositions``.

```iecst
(*
	List of base nest position for Unit 01
    These values are defined at init.
    They could change

	Source: www.hevs.ch
	Author: Cedric Lenoir
	Date: 15 October 2025
*)
{attribute 'qualified_only'}
VAR_GLOBAL
    // Base positions for Z axis.
    C_Axis_Z_SafePosition  : LREAL := 0;       // Mean after resetting
    C_Axis_Z_DownPosition  : LREAL := -120;    // 
    
    // Base position of the plate
    // Could be modified after calibration    
    // If using MCS, you should be able to use 0
    C_X_StartingPosition   : LREAL := 0;
    C_Y_StartingPosition   : LREAL := 0;
    C_Z_StartingPosition   : LREAL := 0;
	
    C_Gripper_Open         : BOOL := TRUE;
    C_Gripper_Close        : BOOL := FALSE; 

// Position for left plate
// That is: QR code on left front of the plate
//	Nest description
//	O	O	O
//	O	O	O
//	O	O	O
//		O	O
//		O	O

// Nest Numbers
//	1	4	9
//	2	5	10
//	3	6	11
//		7	12
//		8	13

    NestNumber_1_X_AxisOffsetPosition : LREAL  := 10;
    NestNumber_1_Y_AxisOffsetPosition : LREAL  := 160;
    NestNumber_1_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;

    NestNumber_2_X_AxisOffsetPosition : LREAL  := 10;
    NestNumber_2_Y_AxisOffsetPosition : LREAL  := 120;
    NestNumber_2_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_3_X_AxisOffsetPosition : LREAL  := 10;
    NestNumber_3_Y_AxisOffsetPosition : LREAL  := 80;
    NestNumber_3_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_4_X_AxisOffsetPosition : LREAL  := 80;
    NestNumber_4_Y_AxisOffsetPosition : LREAL  := 160;
    NestNumber_4_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_5_X_AxisOffsetPosition : LREAL  := 80;
    NestNumber_5_Y_AxisOffsetPosition : LREAL  := 120;
    NestNumber_5_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_6_X_AxisOffsetPosition : LREAL  := 80;
    NestNumber_6_Y_AxisOffsetPosition : LREAL  := 80;
    NestNumber_6_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_7_X_AxisOffsetPosition : LREAL  := 80;
    NestNumber_7_Y_AxisOffsetPosition : LREAL  := 40;
    NestNumber_7_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_8_X_AxisOffsetPosition : LREAL  := 80;
    NestNumber_8_Y_AxisOffsetPosition : LREAL  := 0;
    NestNumber_8_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_9_X_AxisOffsetPosition : LREAL  := 150;
    NestNumber_9_Y_AxisOffsetPosition : LREAL  := 160;
    NestNumber_9_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_10_X_AxisOffsetPosition : LREAL  := 150;
    NestNumber_10_Y_AxisOffsetPosition : LREAL  := 120;
    NestNumber_10_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_11_X_AxisOffsetPosition : LREAL  := 150;
    NestNumber_11_Y_AxisOffsetPosition : LREAL  := 80;
    NestNumber_11_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_12_X_AxisOffsetPosition : LREAL  := 150;
    NestNumber_12_Y_AxisOffsetPosition : LREAL  := 40;
    NestNumber_12_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;
    
    NestNumber_13_X_AxisOffsetPosition : LREAL  := 150;
    NestNumber_13_Y_AxisOffsetPosition : LREAL  := 0;
    NestNumber_13_Z_AxisOffsetPosition : LREAL  := C_Axis_Z_DownPosition;   
END_VAR

```