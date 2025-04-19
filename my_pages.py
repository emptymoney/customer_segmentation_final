import pandas as pd
import pickle
import my_functions as fn

df_RFM=pd.read_csv('files/df_RFM.csv')
df_full=pd.read_csv('files/df_full.csv')
df_name=pd.read_csv('files/df_name.csv')
df_now=pd.read_csv('files/df_now.csv')
rfm_agg=pd.read_csv('files/rfm_agg.csv')
df_SoSanhThuatToan=pd.read_csv('files/SoSanhThuatToan.csv',delimiter=';')

df_RFM_TapLuat=pd.read_csv('files/df_RFM_TapLuat.csv')
rfm_agg_TapLuat=pd.read_csv('files/rfm_agg_TapLuat.csv')

df_now_gmm=pd.read_csv('files/df_now_gmm.csv')
rfm_agg_gmm=pd.read_csv('files/rfm_agg_gmm.csv')

kmeans_model=pickle.load(open('models/kmeans_model.pkl', 'rb'))

#-------------------------------------------------------------
def trang_chu(st):
    st.markdown("<h1 style='text-align: center;'>Đồ Án Tốt Nghiệp<br>Data Science & Machine Learning</h1>", unsafe_allow_html=True)    
    st.markdown("<h2 style='text-align: center;font-weight: bold; color: blue'>Đề tài: Phân nhóm khách hàng</h2>", unsafe_allow_html=True)
    st.image('images/h3_1.png')

# -----------------------------------------------------------------------------------
def yeu_cau_cua_doanh_nghiep(st):
    image_path = "images/CuaHang2.jpg"  # Thay bằng đường dẫn của bạn
    st.image(image_path, use_container_width=True)     
    fn.yeu_cau_cua_doanh_nghiep(st)

# -----------------------------------------------------------------------------------

def cac_thuat_toan_thu_nghiem(st):
    tab1, tab2, tab3,tab4 = st.tabs(["BIỂU ĐỒ PHÂN PHỐI RFM","TẬP LUẬT", "THUẬT TOÁN GMM", "THUẬT TOÁN K-MEANS"])   
    with tab1:   
        fn.plot_distribution(st,df_RFM[['Recency']], "Phân phối Recency", "Recency")
        st.divider()
        fn.plot_distribution(st,df_RFM[['Frequency']], "Phân phối Frequency", "Frequency")
        st.divider()
        fn.plot_distribution(st,df_RFM[['Monetary']], "Phân phối Monetary", "Monetary") 
    with tab2:
        st.write("### Tập Luật chia làm 5 nhóm") 
        st.write("**Tính giá trị trung bình RFM cho các nhóm**")
        st.markdown(fn.format_table(rfm_agg_TapLuat).to_html(), unsafe_allow_html=True)
        fn.ve_cac_bieu_do(rfm_agg_TapLuat,df_RFM_TapLuat,st,'Tập luật')
    with tab3:
        st.write("### GMM chia làm 5 nhóm")
        rfm_agg_gmm.rename(columns={'Cluster':'ClusterName'},inplace=True)
        df_now_gmm.rename(columns={'Cluster':'ClusterName'},inplace=True)
        df_now_gmm['ClusterName']='Cluster '+ df_now_gmm['ClusterName'].astype(str)
        st.markdown(fn.format_table(rfm_agg_gmm).to_html(), unsafe_allow_html=True)
        fn.ve_cac_bieu_do(rfm_agg_gmm,df_now_gmm,st,'GMM')
    with tab4:
        st.write("### KMeans với k=6 ,chia làm 6 nhóm")
        st.markdown(fn.format_table(rfm_agg).to_html(), unsafe_allow_html=True)
        fn.ve_cac_bieu_do(rfm_agg,df_now,st,'KMeans')         

  

# -----------------------------------------------------------------------------------
def lua_chon_ket_qua(st):
    st.markdown("<h2 style='text-align: center;'>Chọn thuật toán K-Means để làm thử nghiệm phân nhóm khách hàng</h2>", unsafe_allow_html=True) 
    st.markdown("<h3 style='text-align: center;font-weight: bold; color: blue'>Sử dụng k=6 -> Chia thành 6 nhóm</h3>", unsafe_allow_html=True)    

    tab1, tab2,tab3 = st.tabs(["BẢNG SO SÁNH CÁC THUẬT TOÁN","CÁC PHÂN KHÚC KHÁCH HÀNG", "TOP 3 SẢN PHẨM/NHÓM SẢN PHẨM"])   
    with tab1:
        st.write("**Bảng so sánh các thuật toán**")
        fn.so_sanh_cac_thuat_toan(st,df_SoSanhThuatToan)
        st.divider()
        fig_scatter_3d_data=fn.truc_quan_hoa_scatter_3d_data(df_now,'KMeans')
        st.plotly_chart(fig_scatter_3d_data) 
        st.divider()
        st.write("""
                 **Từ biểu đồ scatter 3D cho thấy**
                 - Các cụm khách hàng được phân tách rõ ràng
                 - Không chồng lấn  
                 - Phân tán đồng đều

                 **Từ bảng so sánh ta cần một thuật toán:**
                 - Có tốc độ nhanh, đơn giản
                 - Dễ tính toán và kiểm tra

                 -> Ta nhận thấy rằng K-Means là thuật toán khá phù hợp trong trường hợp này                 
                 """)       

        st.markdown("<h4 style='text-align: center; color:'>Chọn <span style='color: blue;'>K-Means</span> làm thuật toán để phát triển ứng dụng</h4>", unsafe_allow_html=True) 
    with tab2:
        fig=fn.truc_quan_hoa_treemap(rfm_agg,'KMeans')
        st.plotly_chart(fig)
        st.write("##### Giải thích ClusterName:")
        fn.giai_thich_ClusterName(st,'Diamond Customers')
        fn.giai_thich_ClusterName(st,'Loyal Customers')
        fn.giai_thich_ClusterName(st,'Regular Customers')
        fn.giai_thich_ClusterName(st,'Potential Customers')
        fn.giai_thich_ClusterName(st,'New Customers')
        fn.giai_thich_ClusterName(st,'Lost Customers')  
    with tab3:
        top_products_per_cluster, top_category_per_cluster, top_products_amount_per_cluster=fn.get_top_products_cluster_info(df_full,3)

        fig1=fn.draw_top_products_cluster_info(
            y='items',
            ylabel='Số lượng bán',
            hue='productName',
            title='Top 3 sản phẩm (Product) có số lượng bán lớn nhất trong mỗi Cluster',
            legend_title='Sản phẩm',
            data=top_products_per_cluster)
        fig1.update_layout(height=500)
        st.plotly_chart(fig1)
        st.divider()

        fig2=fn.draw_top_products_cluster_info(
            y='items',
            ylabel='Số lượng bán',
            hue='Category',
            title='Top 3 nhóm sản phẩm (Category) có số lượng bán lớn nhất trong mỗi Cluster',
            legend_title='Nhóm sản phẩm',
            data=top_category_per_cluster)     
        fig2.update_layout(height=500) 
        st.plotly_chart(fig2)
        st.divider()             

        fig3=fn.draw_top_products_cluster_info(
            y='amount',
            ylabel='Tổng amount',
            hue='productName',
            title='Top 3 sản phẩm (Product) có tổng giá bán (amount) lớn nhất trong mỗi Cluster',
            legend_title='Sản phẩm',
            data=top_products_amount_per_cluster)  
        fig3.update_layout(height=500)
        st.plotly_chart(fig3)             
        st.divider()
     
# -----------------------------------------------------------------------------------
def ung_dung_phan_nhom(st):   
    st.write("### 📈Dự đoán và Phân nhóm Khách hàng")   
    status = st.radio("**Chọn cách nhập thông tin khách hàng:**", ("🆔Nhập id khách hàng là thành viên của cửa hàng:", "📊Nhập RFM của khách hàng:","📤Upload file chứa thông tin mã khách hàng cùng với RFM:"))   

    st.write(f'**{status}**')
    if status=="🆔Nhập id khách hàng là thành viên của cửa hàng:":
        list_customers=fn.get_list_customers(df_full)   
        fn.select_one_customers_by_id(list_customers,df_full,st)        
    elif status=='📊Nhập RFM của khách hàng:':                
        fn.select_one_customers_by_RFM(df_full,df_name,kmeans_model,st)
    elif status=='📤Upload file chứa thông tin mã khách hàng cùng với RFM:':    
        st.write("**⏬Download file mẫu tại đây:**")  
        fn.download_file(st,'files/file_mau.csv')
        st.write("**⏫Upload file để phân nhóm tại đây:**")        
        fn.upload_customers_file(st,kmeans_model,df_name) 

# ===================================================================================
if __name__ == "__main__":
    pass    