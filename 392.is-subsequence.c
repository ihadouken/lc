// bool isSubsequence(char * s, char * t){
//     int i, j;
//     i = j = 0;
//
//     if (s[j] == '\0')
//         return true;
//
//     while (t[i] != '\0') {
//         if (t[i] == s[j]) {
//             j++;
//             if (s[j] == '\0')
//                 return true;
//         }
//         i++;
//     }
//
//     return false;
// }


bool isSubsequence(char * s, char * t){
    int i, j;
    i = j = 0;

    while (s[j] != '\0' && t[i] != '\0') {
        if (s[j] == t[i])
            j++;
        i++;
    }

    return s[j] == '\0';
}
