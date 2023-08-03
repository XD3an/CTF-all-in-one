# rotation

## Information

### Description

You will find the flag after decrypting this file
Download the encrypted flag here.

### Hints

1. Sometimes rotation is right

## Solution

- [Caser Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

### Script
```py
class CaserCipher:
    def __init__(self):
        pass
    # Encrypto  
    def encrypto_caser(self, plaintext, n):
        '''
            C = (P + k) mod 26
        '''
        # Declare a string
        result = str()
        # Encrypt 0 to len(text)
        for i in range(len(plaintext)):
            # temporary storage each char to a
            a = plaintext[i]
            # Encrypt 'A'-'Z' & 'a'-'z' 
            if (65 <= ord(a) and ord(a) <= 90) or ( 97 <= ord(a) and ord(a) <= 122):
                if (65 <= ord(a) and ord(a) <= 90):      # uppercase
                    result += chr((ord(a)+n-65)%26+65)
                elif (97 <= ord(a) and ord(a) <= 122):   # lowercase                          
                    result += chr((ord(a)+n-97)%26+97)
            else:
                result += plaintext[i]
        # return result(cipher text)
        return result
    
    
    # decrypto
    def decrypto_caser(self, ciphertext, n):
        '''
            p = (C - k) mod 26
        '''
        result = str()
        for i in range(len(ciphertext)):
            a = ciphertext[i]
            if (65 <= ord(a) and ord(a) <= 90 or (97 <= ord(a) and ord(a) <= 122)):
                if (65 <= ord(a) and ord(a) <= 90):
                    result +=  chr((ord(a)-n-65)%26+65)
                elif (97 <= ord(a) and ord(a) <= 122):
                    result += chr((ord(a)-n-97)%26+27)
            else:
                result += plaintext[i]
        return result
        
    # brute force attack
    def brute_force(self, ciphertext):
        # Testing 26 times (using all shift possible)
        for n in range(26):
            # Declare a string
            result = str()
            # Decrypto 0 to len(cipher)    
            for i in range(len(ciphertext)):
                # temporary storage each char to a
                a = ciphertext[i]
                # Decrypt 'A'-'Z' & 'a'-'z'
                if (65 <= ord(a) and ord(a) <= 90) or ( 97 <= ord(a) and ord(a) <= 122):
                    if (65 <= ord(a) and ord(a) <= 90):      # uppercase
                        result += chr((ord(a)+n-65)%26+65)
                    elif (97 <= ord(a) and ord(a) <= 122):   # lowercase   
                        result += chr((ord(a)+n-97)%26+97)
                else:
                    result += ciphertext[i]
            # print result possible
            print(result)

if __name__=='__main__':
    CaserCipher = CaserCipher()

    # brute force
    print("Brute force attack case: ") 
    ciphertext = input("cipher text: ")
    print(f"\"{ciphertext}\" to plain text (Bute-force attack)")
    CaserCipher.brute_force(ciphertext)
```

- Usage
    ```sh
    python flag.py
    Brute force attack case: 
    cipher text: xqkwKBN{z0bib1wv_l3kzgxb3l_jln2n252}
    "xqkwKBN{z0bib1wv_l3kzgxb3l_jln2n252}" to plain text (Bute-force attack)
    xqkwKBN{z0bib1wv_l3kzgxb3l_jln2n252}
    yrlxLCO{a0cjc1xw_m3lahyc3m_kmo2o252}
    zsmyMDP{b0dkd1yx_n3mbizd3n_lnp2p252}
    atnzNEQ{c0ele1zy_o3ncjae3o_moq2q252}
    buoaOFR{d0fmf1az_p3odkbf3p_npr2r252}
    cvpbPGS{e0gng1ba_q3pelcg3q_oqs2s252}
    dwqcQHT{f0hoh1cb_r3qfmdh3r_prt2t252}
    exrdRIU{g0ipi1dc_s3rgnei3s_qsu2u252}
    fyseSJV{h0jqj1ed_t3shofj3t_rtv2v252}
    gztfTKW{i0krk1fe_u3tipgk3u_suw2w252}
    haugULX{j0lsl1gf_v3ujqhl3v_tvx2x252}
    ibvhVMY{k0mtm1hg_w3vkrim3w_uwy2y252}
    jcwiWNZ{l0nun1ih_x3wlsjn3x_vxz2z252}
    kdxjXOA{m0ovo1ji_y3xmtko3y_wya2a252}
    leykYPB{n0pwp1kj_z3ynulp3z_xzb2b252}
    mfzlZQC{o0qxq1lk_a3zovmq3a_yac2c252}
    ngamARD{p0ryr1ml_b3apwnr3b_zbd2d252}
    ohbnBSE{q0szs1nm_c3bqxos3c_ace2e252}
    picoCTF{r0tat1on_d3crypt3d_bdf2f252}
    qjdpDUG{s0ubu1po_e3dszqu3e_ceg2g252}
    rkeqEVH{t0vcv1qp_f3etarv3f_dfh2h252}
    slfrFWI{u0wdw1rq_g3fubsw3g_egi2i252}
    tmgsGXJ{v0xex1sr_h3gvctx3h_fhj2j252}
    unhtHYK{w0yfy1ts_i3hwduy3i_gik2k252}
    voiuIZL{x0zgz1ut_j3ixevz3j_hjl2l252}
    wpjvJAM{y0aha1vu_k3jyfwa3k_ikm2m252}
    ```