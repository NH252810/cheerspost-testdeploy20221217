# ターミナルでfoliumのインポート
# 参考ULR：https://welovepython.net/streamlit-folium/
import streamlit as st                      # streamlit
from streamlit_folium import st_folium      # streamlitでfoliumを使う
import folium                               # folium
from folium import FeatureGroup, LayerControl
import pandas as pd                         # CSVをデータフレームとして読み込む


# 表示するデータを読み込み
df = pd.read_csv('output_ex2.csv')



# 銘柄でのデータを抽出
all_data = df[df["menue"].str.contains("モルツ|アサヒ|エビス")] #全店舗
mlts_data = df[df["menue"].str.contains("モルツ")]
asahi_data = df[df["menue"].str.contains("アサヒ")]
ebis_data = df[df["menue"].str.contains("エビス")]



# セレクトボックス
bland_options = st.sidebar.selectbox(
    'ご希望のビール銘柄をお選びください。',
    ['全店舗','エビス', 'モルツ','アサヒ'])

st.sidebar.write('現在の選択:', bland_options)



# スライダー
price_slider = st.sidebar.slider(
    '1杯の値段で絞り込みができます',
    min_value = 100,
    max_value = 1000,
    value = 500,
    step = 10,
    )
st.sidebar.write('希望価格：100円～', price_slider, '円です。')



all_data = all_data[all_data["price"] <= price_slider]
mlts_data = mlts_data[mlts_data["price"] <= price_slider]
asahi_data = asahi_data[asahi_data["price"] <= price_slider]
ebis_data = ebis_data[ebis_data["price"] <= price_slider]





# 全店舗（all_map)：地図の中心の緯度/経度、タイル、初期のズームサイズを指定
all_map = folium.Map(
    # 地図の中心位置の指定(今回は大阪市北区役所を指定)
    location = [34.7055051, 135.4983028], 
    # タイル（デフォルトはOpenStreetMap)、アトリビュート(attr:右下の出典情報はデフォルト指定時は不要)指定
    tiles = 'OpenStreetMap',
    # ズームを指定
    # 参考URL：https://maps.gsi.go.jp/development/ichiran.html#pale
    zoom_start = 15
)

#全店舗の層を作成
all_group = FeatureGroup(name="モルツ|アサヒ|エビス")

# 全店舗グループにマーカーを差す
all_group_popups = all_data["name"].values.tolist() # popup用の駅名配列
all_group_latlngs = all_data.iloc[:,6:8].values.tolist() # 座標の2次元配列


for i, row in df.iterrows():
    pop=f"{row['name']}<br>【営業時間】{row['open']}"


# 紫のマーカーを全店舗の座標に差し、グループに追加
for name, latlng in zip(all_group_popups, all_group_latlngs): 
    folium.Marker(
        location=latlng, 
        popup = folium.Popup(pop, max_width=300),
        icon = folium.Icon(icon="glass",icon_color="white", color="purple")
    ).add_to(all_group)





# モルツマップ（molts_map)：地図の中心の緯度/経度、タイル、初期のズームサイズを指定
mlts_map = folium.Map(
    # 地図の中心位置の指定(今回は大阪市北区役所を指定)
    location = [34.7055051, 135.4983028], 
    # タイル（デフォルトはOpenStreetMap)、アトリビュート(attr:右下の出典情報はデフォルト指定時は不要)指定
    tiles = 'OpenStreetMap',
    # ズームを指定
    # 参考URL：https://maps.gsi.go.jp/development/ichiran.html#pale
    zoom_start = 15
)

# モルツの層を作成
mlts_group = FeatureGroup(name="モルツ")

# モルツグループにマーカーを差す
mlts_group_popups = mlts_data["name"].values.tolist() # popup用の駅名配列
mlts_group_latlngs = mlts_data.iloc[:,6:8].values.tolist() # 座標の2次元配列


# 青のマーカーをモルツの座標に差し、グループに追加
for name, latlng in zip(mlts_group_popups, mlts_group_latlngs): 
    folium.Marker(
        location=latlng, 
        popup = folium.Popup(pop, max_width=300),
        icon = folium.Icon(icon="glass",icon_color="white", color="darkblue")
    ).add_to(mlts_group)




# アサヒマップ(asahi_map)；地図の中心の緯度/経度、タイル、初期のズームサイズを指定
asahi_map = folium.Map(
    # 地図の中心位置の指定(今回は大阪市北区役所を指定)
    location = [34.7055051, 135.4983028], 
    # タイル（デフォルトはOpenStreetMap)、アトリビュート(attr:右下の出典情報はデフォルト指定時は不要)指定
    tiles = 'OpenStreetMap',
    # ズームを指定
    # 参考URL：https://maps.gsi.go.jp/development/ichiran.html#pale
    zoom_start = 15
)

# アサヒの層を作成
asahi_group = FeatureGroup(name="アサヒ")

# アサヒグループにマーカーを差す
asahi_group_popups = asahi_data["name"].values.tolist() # popup用の駅名配列
asahi_group_latlngs = asahi_data.iloc[:,6:8].values.tolist() # 座標の2次元配列


# 青のマーカーをモルツの座標に差し、グループに追加
for name, latlng in zip(asahi_group_popups, asahi_group_latlngs): 
    folium.Marker(
        location=latlng, 
        popup = folium.Popup(pop, max_width=300),
        icon = folium.Icon(icon="glass",icon_color="white", color="green")
    ).add_to(asahi_group)




# エビスマップ（ebis_map)：地図の中心の緯度/経度、タイル、初期のズームサイズを指定
ebis_map = folium.Map(
    # 地図の中心位置の指定(今回は大阪市北区役所を指定)
    location = [34.7055051, 135.4983028], 
    # タイル（デフォルトはOpenStreetMap)、アトリビュート(attr:右下の出典情報はデフォルト指定時は不要)指定
    tiles = 'OpenStreetMap',
    # ズームを指定
    # 参考URL：https://maps.gsi.go.jp/development/ichiran.html#pale
    zoom_start = 15
)

#エビスの層を作成
ebis_group = FeatureGroup(name="エビス")

#エビスグループにマーカーを差す
ebis_group_popups = ebis_data["name"].values.tolist() # popup用の駅名配列
ebis_group_latlngs = ebis_data.iloc[:,6:8].values.tolist() # 座標の2次元配列


# 青のマーカーをエビスの座標に差し、グループに追加
for name, latlng in zip(ebis_group_popups, ebis_group_latlngs): 
    folium.Marker(
        location=latlng, 
        popup = folium.Popup(pop, max_width=300),
        icon = folium.Icon(icon="glass",icon_color="white", color="orange")
    ).add_to(ebis_group)




# 各銘柄を地図に追加
all_group.add_to(all_map)
mlts_group.add_to(mlts_map)
asahi_group.add_to(asahi_map)
ebis_group.add_to(ebis_map)










#追記 最安値
all_min_price = df["price"].min()
all_mean_price = df["price"].mean()

mlts_min_price = mlts_data["price"].min()
mlts_mean_price = mlts_data["price"].mean()

asahi_min_price = asahi_data["price"].min()
asahi_mean_price = asahi_data["price"].mean()

ebis_min_price = ebis_data["price"].min()
ebis_mean_price = ebis_data["price"].mean()



if bland_options == '全店舗':
    st.write('ビールが飲めるお店')
    st_folium(all_map, width=1200, height=800)
    st.sidebar.write('大阪市北区のビール1杯の最安値は、',all_min_price,'円です')
    st.sidebar.write('大阪市北区のビール1杯の平均価格は、',all_mean_price,'円です')


if bland_options == 'モルツ':
    st.write('モルツが飲めるお店')
    st_folium(mlts_map, width=1200, height=800)
    st.sidebar.write('大阪市北区のモルツビール1杯の最安値は、',mlts_min_price,'円です')
    st.sidebar.write('大阪市北区のモルツビール1杯の平均価格は、',mlts_mean_price,'円です')
    
    

if bland_options == 'アサヒ':
    st.write('アサヒが飲めるお店')
    st_folium(asahi_map, width=1200, height=800)
    st.sidebar.write('大阪市北区のモルツビール1杯の最安値は、',asahi_min_price,'円です')
    st.sidebar.write('大阪市北区のモルツビール1杯の平均価格は、',asahi_mean_price,'円です')


if bland_options == 'エビス':
    st.write('エビスが飲めるお店')
    st_folium(ebis_map, width=1200, height=800)
    ebis_min_price = ebis_data["price"].min()
    ebis_mean_price = ebis_data["price"].mean()



