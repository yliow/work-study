// File: Fraction.h

//-----------------------------------------------------------------------------
// Print fraction modeled by numerator n and denominator d.
//-----------------------------------------------------------------------------
void Fraction_print(int n, int d);

//-----------------------------------------------------------------------------
// The fraction modeled by xn and xd as numerator and denominator, i.e., xn/xd,
// is set to the sum of the fractions modeled by yn/yd and zn/zd, i.e.,
// xn/xd = yn/yd + zn/zd 
//-----------------------------------------------------------------------------
void Fraction_add(int & xn, int & xd,
                  int yn, int yd,
                  int zn, int zd);
