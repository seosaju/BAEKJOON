#include <stdio.h>
#include <math.h>

int main() {
    int n, k;
    double s_var = -1;
    double mean = 0;
    double var;
    double sum = 0;
    scanf("%d %d", &n, &k);

    int num[n];
    for(int i = 0; i < n; i++)
        scanf("%d", &num[i]);

    for(int i = k; i <= n; i++) {
        for (int j = 0; j <= n - i; j++) {
            int f_num[i];
            for (int m = 0; m < i; m++)
                f_num[m] = num[j + m];

            mean = 0;
            for (int m = 0; m < i; m++)
                mean += f_num[m];
            mean = mean / i;

            sum = 0;
            for (int m = 0; m < i; m++)
                sum += (f_num[m] - mean) * (f_num[m] - mean);
            var = sum / i;

            if (var <= s_var || s_var == -1)
                s_var = var;
        }
    }
    printf("%lf", sqrt(s_var));
}
